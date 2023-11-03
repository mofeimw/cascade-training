# Train a Haar (Viola-Jones) Cascade Model

Need at least one positive to generative positives from and a lot of negatives  

`resize.py` to resize all negatives to uniform size  

`rename.sh` to rename all negatives to uniform naming  

`create-samples.sh` creates samples  

`create-vector.sh` creates vector file of all positives  

`train-cascade.sh` starts training the model  
`train-cascade-turbo.sh` allocates much more RAM to the training process for a better model  

Training takes place in stages. Data is written after every stage is completed, which will take longer exponentially. By changing the number of stages parameter to `n + 1`, `n` stages will be loaded in.  

`HR` = Hit Rate, the % of positive samples classified correctly  
`FA` = False Alarm, the % of negative samples incorrectly classified as positive  
High HR, low FA, and low acceptance ratio (n * 10^-4)
