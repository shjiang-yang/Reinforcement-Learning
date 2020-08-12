#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf
import numpy as np
import copy


class Experience_pool():
    def __init__(self, experience_pool_size, observation_space_dim, action_space_dim):
#         [obs, act, r, obs_, done]
        self.exp_pool = np.zeros((experience_pool_size, observation_space_dim*2 + action_space_dim + 1 + 1))
        self.index = 0
        self.experience_pool_size = experience_pool_size
        self.experience_pool_ready = False
    
    
    def add_experience(self, observation, action, reward, observation_, done):
        exp = np.hstack((observation, action, reward, observation_, done))
        exp = exp.astype(np.float32)
        self.exp_pool[self.index, :] = exp 
        
        self.index += 1
        if self.index >= self.experience_pool_size:
            self.index = 0
            self.experience_pool_ready = True
        
        return self.experience_pool_ready
    
    
    def get_minibatch_experience(self, minibatch_size):
        return self.exp_pool[np.random.randint(self.experience_pool_size, size=minibatch_size), :]


class Model(tf.keras.Model):
    def __init__(self, action_space_n):
        super (Model, self).__init__()
        
        self.l1 = tf.keras.layers.Dense(units=128, activation=tf.nn.relu)
        self.l2 = tf.keras.layers.Dense(units=128, activation=tf.nn.relu)
        self.l3 = tf.keras.layers.Dense(units=action_space_n, activation=None)
        
        
    def call(self, inputs):
        h1 = self.l1(inputs)
        h2 = self.l2(h1)
        out = self.l3(h2)
        return out


class DQN_AGENT():
    def __init__(self, action_space_n, action_space_dim, observation_space_dim, experience_pool_size):
        self.q_value_Model = Model(action_space_n=action_space_n)
        self.q_target_Model = Model(action_space_n=action_space_n)

        self.q_value_Model.build(input_shape=(None, observation_space_dim))
        self.q_target_Model.build(input_shape=(None, observation_space_dim))
        
        self.q_target_Model.set_weights(self.q_value_Model.get_weights())
        
        
        self.Experience_pool = Experience_pool(experience_pool_size=experience_pool_size, \
                                                observation_space_dim=observation_space_dim, \
                                                action_space_dim = action_space_dim)
#         define parameters
        self.gamma = 0.9
        self.epsilon = 0.9
        self.epsilon_decrease = 1e-4
        self.learning_steps = 0
        self.target_Model_update_per_step = 100
        
        self.minibatch_size = int(experience_pool_size / 10) 
        self.action_space_n = action_space_n
        self.observation_space_dim = observation_space_dim
        
        self.status_info = {"exp_pool_ready": None, \
                            "epsilon_current": None, \
                            "learning_times": 0, \
                            "target_net_update_times": 0, \
                            "loss": None, \
                            "evaluation_scores": None}
        
    def add_experience(self, observation, action, reward, observation_, done):
        exp_pool_ready = self.Experience_pool.add_experience(observation, action, reward, observation_, done)
        self.status_info["exp_pool_ready"] = exp_pool_ready
        return exp_pool_ready
        
        
    def __get_minibatch_experience(self, minibatch_size):
        return self.Experience_pool.get_minibatch_experience(minibatch_size)
        
    
    def get_action(self, observation, epsilon_greedy=True):
        observation = tf.cast(tf.expand_dims(input=observation, axis=0), dtype=tf.float32)
        eps = max(self.epsilon - self.epsilon_decrease * self.learning_steps, 0.01)
        if tf.random.uniform(shape=(1,)) < eps and epsilon_greedy:
            action = tf.random.uniform(shape=(1,), minval=0, maxval=self.action_space_n, dtype=tf.int32)
        else:
            action = tf.argmax(self.q_value_Model(observation)[0])
        self.status_info["epsilon_current"] = eps
        
        return int(action)
    
    
    def learning(self, ):
        minibatch = tf.cast(self.__get_minibatch_experience(self.minibatch_size), dtype=tf.float32)
        obs = minibatch[:, 0:self.observation_space_dim]      # [b, obs_dims]
        action = minibatch[:, self.observation_space_dim]     # [b]
        reward = minibatch[:, self.observation_space_dim+1]   # [b]
        obs_ = minibatch[:, -self.observation_space_dim-1:-1] # [b, obs_dims]
        done = minibatch[:, -1]                               # [b]

        q_target = reward + self.gamma * tf.reduce_max(self.q_target_Model(obs_), axis=1) * (1. - done)
        
        action_onehot = tf.one_hot(indices=tf.cast(action, tf.int32), depth=self.action_space_n)
        
        with tf.GradientTape() as tape:
            q_value = self.q_value_Model(obs)                # [b, action_space_n]
            q_value_a = q_value * action_onehot
            q_pred = tf.reduce_sum(q_value_a, axis=1)
            
            loss = tf.losses.mse(q_target, q_pred)
            
        grads = tape.gradient(target=loss, sources=self.q_value_Model.trainable_variables)
        tf.optimizers.Adam(learning_rate=1e-3).apply_gradients(zip(grads, self.q_value_Model.trainable_variables))
        
        if self.learning_steps % self.target_Model_update_per_step == 0:
            self.__target_Model_update()
        
        self.learning_steps += 1
        
        self.status_info["loss"] = float(loss)
        self.status_info["learning_times"] += 1

        
        
    def __target_Model_update(self,):
        self.q_target_Model.set_weights(self.q_value_Model.get_weights())
        self.status_info["target_net_update_times"] += 1
        