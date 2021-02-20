%% 
clc; close all; clear all; warning off; 
path = '/home/wangxiao/Documents/rgb_event_tracking_benchmark/visEvent_dataset/test_subset/'; 
files = dir(path);
files = files(3:end); 

for vid =1:size(files, 1)
    videoName = files(vid).name; 
    event_img_files = dir([path videoName '/event_imgs/*.bmp']);
    rgb_img_files   = dir([path videoName '/vis_imgs/*.bmp']);    
    
    savedIMG_path = [path videoName '/fused_imgs/']; 
    mkdir(savedIMG_path); 
    
    for imgID =1:size(event_img_files, 1)
        event_img = imread([path videoName '/event_imgs/' event_img_files(imgID).name]); 
        rgb_img   = imread([path videoName '/vis_imgs/' rgb_img_files(imgID).name]); 
        
        fusedIMG = event_img;
        
        fusedImg1 = imlincomb(0.2,event_img(:, :, 1), 1,rgb_img(:, :, 1));
        fusedImg2 = imlincomb(0.2,event_img(:, :, 2), 1,rgb_img(:, :, 2));
        fusedImg3 = imlincomb(0.2,event_img(:, :, 3), 1,rgb_img(:, :, 3));
        
        fusedIMG(:, :, 1) = fusedImg1; 
        fusedIMG(:, :, 2) = fusedImg2; 
        fusedIMG(:, :, 3) = fusedImg3; 
        
        imwrite(fusedIMG, [savedIMG_path event_img_files(imgID).name]);
        
%         subplot(1,3,1),subimage(event_img);
%         title('image 1');
%         subplot(1,3,2),subimage(rgb_img);
%         title('image 2');
%         subplot(1,3,3),subimage(fusedIMG);
%         title('fused image');


    end 

end 

































































