# This code demonstrates a nueron that looks like :
# input, weight ... 
# 1 *  0.2 → + bias 2 ● → output 2.3
# 2 *  0.8 ↗
# 3 * -O.5 ↗

inputs = [ 1, 2, 3 ]
weights = [ 0.2, 0.8, -0.5 ]
bias = 2
output = ( inputs[0] * weights[0] +
           inputs[1] * weights[1] +
           inputs[2] * weights[2] +
          + bias
          )
print(output)
