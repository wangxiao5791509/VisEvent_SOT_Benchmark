%%
clc; close all; clear all; warning off;
addpath('C:\Users\rj-wang\Documents\jsonlab-1.5\jsonlab-1.5');

fileName = 'part_3_100videos'; 
path = ['C:\Users\rj-wang\Desktop\VisEvent_tracking_dataset-322097\µ„Œ“\' fileName '\'];
anno_path = 'K:\visEvent_tracking_dataset\dataset\';
annoFiles = dir(anno_path);
annoFiles = annoFiles(3:end);

imagePath = ['K:\visEvent_tracking_dataset\dataset\' fileName '\'];

videoFiles = dir(path);
videoFiles = videoFiles(3:end); 

count = 0;
workCount = 0;

% for vidIDX =1:size(videoFiles, 1)
for vidIDX = 43     
    vidIDX
    videoName = videoFiles(vidIDX).name; 
    videoPath = [path videoName '\'];
    jsonFiles = dir([videoPath '*.json']);
    
    imgPath = [imagePath videoName '\vis_imgs\']; 
    imgFiles = dir([imgPath '*.bmp']); 
    
    txtsavePath = [anno_path fileName '\' videoName '\' ]; 
    mkdir(txtsavePath); 
    
    fid = fopen([txtsavePath, 'absent_label.txt'], 'w');
    fid2 = fopen([txtsavePath, 'groundtruth.txt'], 'w');
    
    
    for jsonID =1:size(imgFiles, 1)
        
        % image = imread([imgPath imgFiles(jsonID).name]);
        
        imgNAME = imgFiles(jsonID).name; 
        imgNAME = imgNAME(1:end-4); 
        jsonFIlename = [imgNAME '.json']; 
        
        try 
            json2data=loadjson([videoPath jsonFIlename]);
            
            x1 = json2data.Public{1, 1}.Landmark{1, 1}.Points{1, 1}.X ;
            y1 = json2data.Public{1, 1}.Landmark{1, 1}.Points{1, 1}.Y ;
            
            x2 = json2data.Public{1, 1}.Landmark{1, 1}.Points{1, 2}.X ;
            y2 = json2data.Public{1, 1}.Landmark{1, 1}.Points{1, 2}.Y ;
            
            x3 = json2data.Public{1, 1}.Landmark{1, 1}.Points{1, 3}.X ;
            y3 = json2data.Public{1, 1}.Landmark{1, 1}.Points{1, 3}.Y ;
            
            x4 = json2data.Public{1, 1}.Landmark{1, 1}.Points{1, 4}.X ;
            y4 = json2data.Public{1, 1}.Landmark{1, 1}.Points{1, 4}.Y ;
            pointAll = [x2, y2];    
            windSize = [x4-x2, y4-y2];  
            BBox = [pointAll windSize]; 
            fprintf(fid2, '%s', num2str(BBox(1)));
            fprintf(fid2, ',');
            fprintf(fid2, '%s', num2str(BBox(2)));
            fprintf(fid2, ',');
            fprintf(fid2, '%s', num2str(BBox(3)));
            fprintf(fid2, ',');
            fprintf(fid2, '%s', num2str(BBox(4)));
            fprintf(fid2, '\n');
            

            fprintf(fid, '%s', num2str(1));
            fprintf(fid, '\n');
        catch 
            BBox = [0 0 0 0];
            fprintf(fid2, '%s', num2str(0));
            fprintf(fid2, ',');
            fprintf(fid2, '%s', num2str(0));
            fprintf(fid2, ',');
            fprintf(fid2, '%s', num2str(0));
            fprintf(fid2, ',');
            fprintf(fid2, '%s', num2str(0));
            fprintf(fid2, '\n');
            
            fprintf(fid, '%s', num2str(0));
            fprintf(fid, '\n');            
        end 
        
        %         BBox 
        %         figure; imshow(image);
        %         hold on;
        %         rect = [x1 y1 x3 y3 ];
        %         plot(rect, 'linewidth', 2);
        %         patch = imcrop(image, rect);
        %         figure; imshow(patch);
        
        %         patch = imcrop(image, [pointAll windSize]);
        %         figure; imshow(patch);
        %         [state, results]=draw_rect(image, pointAll, windSize);
        

    end

    fclose(fid);
    fclose(fid2);
    
end




