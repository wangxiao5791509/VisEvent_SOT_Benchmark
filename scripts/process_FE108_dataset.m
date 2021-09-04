%%
clc; close all; clear all; warning off; 
datasetPath = 'K:\FE108_Event_tracking_dataset\seqs\';
startIDX_file = fopen([datasetPath 'start_frame_idx.txt']); 

trainPath = [datasetPath '\train\']; 
testPath  = [datasetPath '\test\']; 

allVideoNames = dir(trainPath);
allVideoNames = allVideoNames(3:end);

while ~feof(startIDX_file)        
    tline=fgetl(startIDX_file);   
    
    middleIDX = strfind(tline, ','); 
    
    videoName = tline(1:middleIDX-1); 
    startIDX = str2double(tline(middleIDX+1:end)); 
    
    dvs_imgs = dir([testPath videoName '\events\events_dvs\*.bmp']); 
    
    aps_imgs = dir([testPath videoName '\img\*.jpg']); 
    aps_imgNUM = size(aps_imgs, 1); 
    
    dvsIMG_savePath = [testPath videoName '\event_imgs\']; 
    mkdir(dvsIMG_savePath); 
    
    for imgID = 1:aps_imgNUM
        imgName = dvs_imgs(startIDX+imgID).name; 
        newDVS_imgName = [sprintf('%04d', imgID) '.bmp']; 
        copyfile([testPath videoName '\events\events_dvs\' imgName], [dvsIMG_savePath newDVS_imgName]);
        disp(['videoName: ', videoName, 'imgIDX: ', newDVS_imgName]); 
    end 
    
    
end
























































































