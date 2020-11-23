var ogimage=null;
var newimage=null;
function upload(){
  var ff1=document.getElementById('file1');
  var cc1=document.getElementById('c1');
  ogimage=new SimpleImage(ff1);
  ogimage.drawTo(cc1);
}

function do_red(){
  if(ogimage==null || !ogimage.complete()){
    alert('The image is not loaded yet!!')
  }
  newimage=new SimpleImage(ogimage.getWidth(),ogimage.getHeight())
  for (var pixel of ogimage.values()){
    var newpixel=newimage.getPixel(pixel.getX(),pixel.getY());
    avg=3*(pixel.getRed(),pixel.getGreen(),pixel.getBlue())/3;
    if(avg<128){
      newpixel.setRed(2*avg);
      newpixel.setGreen(0);
      newpixel.setBlue(0);
    }
    else{
      newpixel.setRed(255);
      newpixel.setGreen(2*avg-255);
      newpixel.setBlue(2*avg-255);

    }
  }
  var cc1=document.getElementById('c1');
  var ctx1=cc1.getContext('2d');
  ctx1.clearRect(0,0,cc1.width,cc1.height);
  newimage.drawTo(cc1)
}

function do_grayscale(){
  if(ogimage==null || !ogimage.complete()){
    alert('The image is not loaded yet!!')
  }
  newimage=new SimpleImage(ogimage.getWidth(),ogimage.getHeight())
  for (var pixel of ogimage.values()){
    var newpixel=newimage.getPixel(pixel.getX(),pixel.getY());
    avg=3*(pixel.getRed(),pixel.getGreen(),pixel.getBlue())/3;
    newpixel.setRed(avg);
    newpixel.setGreen(avg);
    newpixel.setBlue(avg);
  }
  var cc1=document.getElementById('c1');
  var ctx1=cc1.getContext('2d');
  ctx1.clearRect(0,0,cc1.width,cc1.height);
  newimage.drawTo(cc1)
}

function do_sine(){
  if(ogimage==null || !ogimage.complete()){
    alert('The image is not loaded yet!!')
  }
  newimage=new SimpleImage(ogimage.getWidth(),ogimage.getHeight())
  for (var pixel of ogimage.values()){
    var newpixel=newimage.getPixel(pixel.getX(),pixel.getY());
    h=(ogimage.getHeight()/2)*Math.sin(Math.PI*(pixel.getX()/ogimage.getWidth()));
    newpixel.setRed(pixel.getRed());
    if(pixel.getY()>(ogimage.getHeight()-h)){
      newpixel.setGreen(255);
      newpixel.setBlue(pixel.getBlue());
    }
    else{
      newpixel.setGreen(pixel.getGreen());
      newpixel.setBlue(255);
    }
  }
  var cc1=document.getElementById('c1');
  var ctx1=cc1.getContext('2d');
  ctx1.clearRect(0,0,cc1.width,cc1.height);
  newimage.drawTo(cc1)
}

function do_rainbow(){
  if(ogimage==null || !ogimage.complete()){
    alert('The image is not loaded yet!!')
  }
  newimage=new SimpleImage(ogimage.getWidth(),ogimage.getHeight())
  for (var pixel of ogimage.values()){
    var newpixel=newimage.getPixel(pixel.getX(),pixel.getY());
    avg=3*(pixel.getRed(),pixel.getGreen(),pixel.getBlue())/3;
    if(pixel.getY()<ogimage.getHeight()/7){
      if(avg<128){
        newpixel.setRed(2*avg);
        newpixel.setGreen(0);
        newpixel.setBlue(0);
      }
      else{
        newpixel.setRed(255);
        newpixel.setGreen(2*avg-255);
        newpixel.setBlue(2*avg-255);
      }
    }
    else if(pixel.getY()<ogimage.getHeight()*(2/7)){
      if(avg<128){
        newpixel.setRed(2*avg);
        newpixel.setGreen(0.8*avg);
        newpixel.setBlue(0);
      }
      else{
        newpixel.setRed(255);
        newpixel.setGreen(1.2*avg-51);
        newpixel.setBlue(2*avg-255);
      }
    }
    else if(pixel.getY()<ogimage.getHeight()*(3/7)){
      if(avg<128){
        newpixel.setRed(2*avg);
        newpixel.setGreen(2*avg);
        newpixel.setBlue(0);
      }
      else{
        newpixel.setRed(255);
        newpixel.setGreen(255);
        newpixel.setBlue(2*avg-255);
      }
    }
    else if(pixel.getY()<ogimage.getHeight()*(4/7)){
      if(avg<128){
        newpixel.setRed(0);
        newpixel.setGreen(2*avg);
        newpixel.setBlue(0);
      }
      else{
        newpixel.setRed(2*avg-255);
        newpixel.setGreen(255);
        newpixel.setBlue(2*avg-255);
      }
    }
    else if(pixel.getY()<ogimage.getHeight()*(5/7)){
      if(avg<128){
        newpixel.setRed(0);
        newpixel.setGreen(0);
        newpixel.setBlue(2*avg);
      }
      else{
        newpixel.setRed(2*avg-255);
        newpixel.setGreen(2*avg-255);
        newpixel.setBlue(255);
      }
    }
    else if(pixel.getY()<ogimage.getHeight()*(6/7)){
      if(avg<128){
        newpixel.setRed(0.8*avg);
        newpixel.setGreen(0);
        newpixel.setBlue(2*avg);
      }
      else{
        newpixel.setRed(1.2*avg-51);
        newpixel.setGreen(2*avg-255);
        newpixel.setBlue(255);
      }
    }
    else{
      if(avg<128){
        newpixel.setRed(1.6*avg);
        newpixel.setGreen(0);
        newpixel.setBlue(1.6*avg);
      }
      else{
        newpixel.setRed(0.4*avg+153);
        newpixel.setGreen(2*avg-255);
        newpixel.setBlue(0.4*avg+153);
      }
    }
  }
  var cc1=document.getElementById('c1');
  var ctx1=cc1.getContext('2d');
  ctx1.clearRect(0,0,cc1.width,cc1.height);
  newimage.drawTo(cc1)
}

function do_reset(){
  var cc1=document.getElementById('c1');
  ogimage.drawTo(cc1);
}
