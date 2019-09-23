## 强化学习介绍  
---  


### 学习目标  
- 理解强化学习问题，以及与监督学习的区别  
- 利用OpenAI Gym中的强化学习环境  
--- 


### 知识要点  
- 强化学习(reinforecment learning, RL)是有关目标驱动(goal-directed)和做决策(decision-making)的学习算法  
- 在RL中，智能体(agent)从其与环境交互的经验中进行学习，而监督学习不与环境交互  
- agent的奖励(reward)通常是延迟的，agent的目标是最大化累计奖励值，因为最终的目标通常经次优的行为实现  
- agent与环境(environment)交互的数据包括 [state, reward, action]  
--- 


### 学习笔记  
#### **1** [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/RLbook2018.pdf) - Chapter 1： Introduction  
机器学习方法可分为三种，即监督学习、无监督学习、强化学习。监督学习是训练一个模型来拟合给定的带标签的训练数据集，以预测训练集以外的情况；无监督学习是在给定的无标签的数据中训练一个模型将具有一定相似特征的数据聚类在一起；强化学习是从自己与环境交互的经验中学习，其目标是最大化累计奖励，方法是试错与行为评估。  

在强化学习中，agent必须能够感知环境的状态，施加的动作也必须能够改变环境的状态，环境中必须存在表示完成目标的状态。强化学习的三个重要特点：试错、奖励延迟、环境交互。强化学习的经验数据是从与环境交互中获得的。强化学习的挑战之一是权衡探索(exploration)与利用(exploitation)，agent为了获得奖励，既要利用尝试过的能够获得奖励的动作取得奖励，又要探索更多的动作空间，以发现能够获得奖励的行为。  

强化学习的学习模式是最接近人类和其他动作的学习模式。举个例子：初生的小绵羊能够在落地一两个小时之后活蹦乱跳。其中有几点值得注意：  
> - 小绵羊的目标是用四脚行走，但是初生时并不会  
> - 一两个小时之内，小绵羊不断尝试站起来行走，也不断摔倒  
> - 当小绵羊站起来后，其大脑会给一个积极的奖励信号  
> - 小绵羊能感知环境状态，其动作也能改变环境  

强化学习也有这些特点。  

强化学习的组成要素包括：agent、environment、reward signal、policy、value function。agent是编程者主体能控制的部分；environment是agent身处的环境，agent不能控制其但是与其交互；policy可以认为是在特定状态下采取哪个动作最佳，即状态到动作的映射关系；reward signal定义了强化学习问题，其定义了状态的好坏，但是reward是瞬时的，奖励值低说明agent本次表现不佳，可能需要改变policy了；value function表示了特定状态在完成目标的过程中的价值，即从给定状态起能够获得的累计奖励的预测，某个状态的奖励低不能说明其价值低，其状态可能是实现目标的必要步骤。  

局限（WIP）

#### **2** [David Silver's RL Course Lecture 1 - Introduction to Reinforcement Learning](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/intro_RL.pdf)  



#### **3** [OpenAI Gym tutorial](https://gym.openai.com/docs)  


--- 


### 练习  
- [调用OpenAI Gym环境](OpenAI_Gym_EnvTest.py)  
