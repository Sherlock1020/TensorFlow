#coding:utf-8
#设损失函数 loss=(w+1)^2, 令w初值是常数5。反向传播就是求最优w，即求最小loss对应的w值。
#使用指数衰减的学习率，在迭代初期得到较高的下降速度，可以在较小的训练轮数下取得更优收敛度

import tensorflow as tf

LEARNING_RATE_BASE = 0.1#最初学习率
LEARNING_RATE_DECAY = 0.99#学习率衰减率
LEARNING_RATE_STEP = 1#喂入多少轮BATCH——SIZE后，更新一次学习率，一般设为：总样本数/BATCH_SIZE

#运行了几轮BATCH_SIZE的计数器，初值为0，设为不被训练
global_step = tf.Variable(0,trainable=False)
#定义指数下降学习率
learning_rate = tf.train.exponential_decay(LEARNING_RATE_BASE,global_step,LEARNING_RATE_STEP,LEARNING_RATE_DECAY,staircase=True)
#定义待优化参数，初值赋5
w = tf.Variable(tf.constant(5,dtype=tf.float32))
#定义反向传播方法
loss = tf.square(w+1)
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(loss,global_step = global_step)
#生成会话，训练40轮
with tf.Session() as sess:
	init_op = tf.global_variables_initializer()
	sess.run(init_op)
	STEPS = 40
	for i in range(STEPS):
		sess.run(train_step)
		learning_rate_val = sess.run(learning_rate)
		global_step_val = sess.run(global_step)
		w_val = sess.run(w)
		loss_val = sess.run(loss)
		print"After %s trainings, learning_rate is %s, global_step is %s, w is %s, loss is %s"%(i,learning_rate_val,global_step_val,w_val,loss_val)
