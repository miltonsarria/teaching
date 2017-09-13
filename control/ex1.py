import control as ctrl
import matplotlib.pyplot as plt


#Define a basic system, numerator, denominator, then the transfer function
num = [1., 2.]
den = [9., 8., 7.]
sys1 = ctrl.tf(num, den)
print sys1
#step and impulse  response
T1, yout1 = ctrl.step_response(sys1)
T2, yout2 = ctrl.impulse_response(sys1)

plt.subplot(211)
plt.plot(T1,yout1)
plt.title('step response')

plt.subplot(212)
plt.plot(T2,yout2)
plt.title('impulse response')

ctrl.root_locus(sys1)

plt.show()

#Create a MIMO transfer function object
num = [[[1., 2.], [3., 4.]], [[5., 6.], [7., 8.]]]
den = [[[9., 8., 7.], [6., 5., 4.]], [[3., 2., 1.], [-1., -2., -3.]]]
sys2 = ctrl.tf(num, den)

