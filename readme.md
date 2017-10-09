

Let's define the problem space - 
   * Dataset: 
     * I have finished parsing and finding data in the `Data/` folder. They have been added in .gitignore file
   * Framwork: Tensorflow (working off of wavenet implementation)
   * Architecture: Sequence to Sequence generation with Deep RNN and RBM
   
NextStep:
   * We need to preprocess those files into their audio signals
   * We need to setup training and get a good accuracy rate
   
Goal: output unique net-generated music piece of classical piano music.

Optional: I wonder how well will GAN perform on this.


=================



Using:
	[ ✓ ] TensorFlow	
	[ x ] WaveNet (not using currently beacuse the examples are all text-to-speech)
	[ x ] Music RNN RBM (not using, was written for TF 0.6 and Py 2.7, could not get to work with any installation of TF and dependencies. Moving on)
	[ x ] Magenta - (not using, py 2.7) using Py 2.7 and miniconda. Installation instructions https://github.com/tensorflow/magenta
		Note that Magenta wants you to create its own virtualenv. Install:
			1. curl https://raw.githubusercontent.com/tensorflow/magenta/master/magenta/tools/magenta-install.sh > /tmp/magenta-install.sh
			2. bash /tmp/magenta-install.sh		
	[ ? ] Simple TF tutorial without a framework: http://danshiebler.com/2016-08-10-musical-tensorflow-part-one-the-rbm/ 

Architecture description: Sequence to sequence generation with deep RNN and RBM

Training data: Classical music pieces (e.g. Bach BWV 1-100)

Goal: output unique net-generated music piece of classical style


Notes:
	https://www.youtube.com/watch?v=SacogDL_4JU&t=847s
