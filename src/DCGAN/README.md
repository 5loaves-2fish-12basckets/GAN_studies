# week2 project: Deep Convolution Generative Adversarioal Networks (DCGAN)

[Goal:] to implement the paper [Unsupervised Representation Learning with Deep Convolutional Generative Adversarial Networks](http://arxiv.org/abs/1511.06434)

### usage:
run experiments with `python experiments/<python script>`

### Initial Results
* MNIST for learning rate = 0.0002 (Adam optimizer), batch size = 128, # of epochs = 40:
<table align='center'>
<tr align='center'>
<td> GAN losses</td>
<td> Generated images</td>
</tr>
<tr>
<td><img src = 'other/basic_mnist_loss_plots.gif'>
<td><img src = 'other/basic_mnist_generated_imgs.gif'>
</tr>
</table>


<!-- * lsun bedroom for learning rate = 0.0002 (Adam optimizer), batch size = 128, # of epochs = 40:
<table align='center'>
<tr align='center'>
<td> GAN losses</td>
<td> Generated images</td>
</tr>
<tr>
<td><img src = 'other/basic_lsun_loss_plots.gif'>
<td><img src = 'other/basic_lsun_generated_imgs.gif'>
</tr>
</table> -->

<!-- ## Tabel of Contents -->
<!-- * [Experiments and Results](other/report.md)   -->


### references: 
* [ErrorLog](other/errorlog.md)
* other codes: https://github.com/togheppi/DCGAN/blob/master/README.md

## Todo:
* compare large, medium, small size models
* reproduce arithemetic effects as stated in paper (with lsun dataset)