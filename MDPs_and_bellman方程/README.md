## MDPs and Bellman方程  
---  


### 学习目标  
- 理解agent与env交互的接口  
- 理解Markov决策过程（MDPs）和transition diagrams  
- 理解value function、action-value function、policy function  
- 理解bellman方程、value function和action-value function的bellman优化方程  

---  
### 知识要点  
- agent与env的交互接口  
   - 在step t时，agent接收到env的当前状态s_t  
   - agent根据policy function π选择一个动作A_t施加给环境  
   - agent接收到奖励值R_(t+1)和下一个状态s_(t+1)  
- 从当前时刻t起，未来的所有奖励之和是G_t，通常未来时刻的奖励值有折扣因子gamma^(k_n-k-1)  
- markov性质：环境在t+1时刻的响应只取决于t时刻的state和action，即未来与现在的过去无关。即使环境不完全满足Markov性，仍然可以尝试构建近似满足Markov性的状态表达式。  
- Markov决策过程由状态集S、动作集A，环境状态转移概率P(s', r | s, a)定义。如果环境模型已知，我们就知道环境状态转移概率，但是，通常是不知道的，只知道是一个Markov决策过程。  
- value function v(s)表征特定状态state对agent的好坏，其是未来累积奖励值G_t的期望，即v(s)=Ex[G_T | S_t=s]。对于给定policy π，value function是一定的。  
- action-value function q(a, s)表示在特定状态state，采取动作action对agent的好坏。与value function类似，但是考虑了action。  
- bellman方程表达了某个状态s的value和目标状态s*的value之间的关系，从backup图中可以直观地看出。value function和action-value function中都有bellman方程。  
- value function反映了policy的好坏。如果对于所有状态都有v_p1(s) > v_p2(s)，则策略p1比p2更好。在MDPs中，总有一个或多个最优化策略。  
- 对于最优化policy，对应着最优值函数v*(S)和q*(a, s)。bellman优化方程表示了某个状态s的最优value和目标状态s*的最优value之间的关系。  

---  
### 学习笔记  
#### #1 [Reinforcement Learning: An Introduction](http://incompleteideas.net/book/RLbook2018.pdf) - Chapter 3: Finite Markov Decision Processes  


#### #2 [David Silver's RL Course Lecture 2 - Markov Decision Processes](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching_files/MDP.pdf)  


--- 
### 练习  


