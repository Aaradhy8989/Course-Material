
# Author @aaradhy
# HP

import matplotlib.pyplot as plt
import numpy
import pandas as pd
from tqdm import tqdm
from sklearn.metrics import mean_squared_error

"""
1. Three figures (mona, ball, cat) are given in .txt format. Each figure is a 90x100 matrix.
a. Visualize the images and make sure that the black pixels are represented by -1 and white pixels
are represented by +1.
"""
#Image_vector converts .txt image into vector and returns the image vector 
def Image_vector(Imagename):
    
    df=pd.read_csv(Imagename+'.txt',header=None)
    #df==[90 rows x 100 columns] containing data points
    Image_arr=numpy.array(df)
    #name_arr==image data in vector 
    Image_arr=numpy.sign(Image_arr)
    plt.imshow(Image_arr,cmap='Greys_r')
    plt.title(f'{Imagename} image')
    plt.show()
    return Image_arr


    
ball=Image_vector('ball') # 'ball' saved file name
mona=Image_vector('mona') # 'mona' saved file name 
cat=Image_vector('cat') 


"""
b. Develop a code for Hopfield network with N=9000 neurons which are fully connected 

2. Save the image of ball in the network
a. Initialize a zero matrix of the same size as that of the input image and replace a small patch
with a portion of the input image as shown in figure 1. Use this (figure 1.B) as the cue for
retrieving the image
b. Plot the patch which is given as the input trigger
c. Plot the Root Mean Squared (RMS) error with time 
"""
#size of ball matrix (90*100)
vec_size=ball.shape[0]*ball.shape[1]
u=numpy.zeros(vec_size)

#changing_dimension
ball_reshaped=numpy.reshape(ball,(vec_size,1))
cat_reshaped=numpy.reshape(cat,(vec_size,1))
mona_reshaped=numpy.reshape(mona,(vec_size,1))


class Hopfield_Network():
    def __init__(self,num_iter):
        self.V = numpy.zeros((9000,1))
        self.U = numpy.zeros((9000,1))
        self.weights = numpy.zeros((9000,9000))
        self.U_d = numpy.zeros((9000,1))
        self.rms_error = numpy.zeros((num_iter,1))
        self.flag = 0 # to load Images
        
    def load_weights(self):

        if self.flag==1:
            print('Loading all images')
            #numpy.matmul(a,b) product a,b
            self.weights = numpy.matmul(mona_reshaped,mona_reshaped.T) + numpy.matmul(ball_reshaped,ball_reshaped.T) + numpy.matmul(cat_reshaped,cat_reshaped.T)
        
        if self.flag==0:
            print('Loading the image of the cat')
            self.weights = numpy.matmul(ball_reshaped,ball_reshaped.T)
        
    def image_loader(self,image):
        '''
        Loads patches of images
        '''
        new_image = numpy.zeros((90,100))
        new_image[0:45,40:65] = image[0:45,40:65]
        return new_image
        
    def damage_weights(self,p):
       
        '''
        Damages the weights of the network with probability p
        '''
        
        indices = numpy.random.randint(0,9000*9000-1,int(9000*9000*p))
        weights_damaged=numpy.copy(self.weights)
        weights_damaged=numpy.reshape(weights_damaged,(9000*9000,1))
        print('Assigning the weights to zero')
        for i in tqdm(range(len(indices))):
            weights_damaged[indices[i]]=0
        weights_damaged = numpy.reshape(weights_damaged,(9000,9000))
        return weights_damaged
            
                
        
        
def demo(num_iter,lambdas,flag,p):
    dt=1/(100)
    Hop_net1=Hopfield_Network(num_iter)
    Hop_net1.flag=flag
    Hop_net1.load_weights()
    Hop_net1.U = numpy.reshape(Hop_net1.image_loader(cat),(9000,1)) #change ball to cat or mona for taking patch of those images
    Hop_net1.weights=Hop_net1.damage_weights(p)
    Hop_net1.weights=Hop_net1.weights/9000
    images_arr=[]
    for i in tqdm(range(num_iter)):
        Hop_net1.U_d = -Hop_net1.U + numpy.matmul(Hop_net1.weights,Hop_net1.V)
        Hop_net1.U = Hop_net1.U + (Hop_net1.U_d)*dt
        Hop_net1.V = numpy.tanh(lambdas*Hop_net1.U)
        Hop_net1.rms_error[i]=mean_squared_error(cat_reshaped,Hop_net1.V) #change ball to cat or mona for taking patch of those images
        
        img=numpy.reshape(Hop_net1.V,(90,100))
        images_arr.append(img)
    images_arr=numpy.array(images_arr)
    return images_arr,Hop_net1.rms_error
    
def show(images_arr,rms_error,num_iter,p):
    images_arr=numpy.array(images_arr)
    for i in range(int(num_iter/10)):
        plt.imshow(images_arr[10*i,:,:],'Greys_r')
        plt.title(f'After {10*i} iterations, {p*100}% weight diff')
        plt.savefig(f'After {10*i} iterations, {p*100}% weight diff'+'.png', dpi=300)
        plt.clf()
        
    plt.plot(rms_error)
    plt.title(f'rms_error, {p*100}% weight diff')
    plt.xlabel('Number of iterations')
    plt.ylabel('rms_error')
    plt.grid()
    plt.savefig(f'rms_error, {p*100}% weight diff'+'.png', dpi=300)
    plt.clf()


"""
3. Save all three images (mona, ball and cat) in the network
a. Give small patches of each image to retrieve the corresponding saved image.
b. Plot the RMS error with time and the final retrieved image for all three inputs.
c. Make X% of weights to be zero and repeat questions 3.a and 3.b for X=25%, X=50% and
X=80%
i. Plot the RMS error with time for each case
ii. Plot the final retrieved image for each case
"""  
num_iter=50
#images with 0% diff and ploting image and iteration
images_arr,rms_error=demo(num_iter,10,0,0)
show(images_arr,rms_error,num_iter,0)       
 #for cat and mona change the image_arr


#running this for ball,mona,cat
num_iter=100

# loading all images with 25% diff and ploting image and iteration
images_arr,rms_error=demo(num_iter,10,1,0.25)   
show(images_arr,rms_error,num_iter,0.25)

# loading all images with 50% diff and ploting image and iteration
images_arr,rms_error=demo(num_iter,10,1,0.5)   
show(images_arr,rms_error,num_iter,0.5)

 # loading all images with 80% diff and ploting image and iteration
images_arr,rms_error=demo(num_iter,10,1,0.8)  
show(images_arr,rms_error,num_iter,0.8)