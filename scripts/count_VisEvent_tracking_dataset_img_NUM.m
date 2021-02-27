%%
clc; close all;

path = '/media/wangxiao/Elements/visEvent_tracking_dataset/';
files = dir(path);
files = files(3:end);

range_1_100 = 0;
range_101_300 = 0;
range_301_500 = 0;
range_500_700 = 0;
range_701_1000 = 0;
range_1000 = 0;

videoNUM = 0;

min_frames  = 0;
mean_frames = 0;
max_frames  = 0;
total_frame = 0;


for id = 12:20
    % for id = 19
    fileName = files(id).name;
    filepath = [path fileName];
    videofiles = dir(filepath);
    videofiles = videofiles(3:end);
    
    for iid = 1:size(videofiles, 1)
        videoNUM = videoNUM + 1;
        disp(['==>> ', num2str(id), ' |', num2str(iid)]);
        videoname = videofiles(iid).name;
        %         %%
        %         imagefiles = dir([path fileName '/' videoname '/vis_imgs/*.bmp']);
        %         if size(imagefiles, 1) == 0
        %             imagefiles = dir([path fileName '/' videoname '/vis_imgs/*.jpg']);
        %         end
        %         if size(imagefiles, 1) == 0
        %             imagefiles = dir([path fileName '/' videoname '/vis_imgs/*.png']);
        %         end
        
        imgfiles = dir([path fileName '/' videoname '/']);
        imgfiles = imgfiles(3:end);
        
        
        if exist([path fileName '/' videoname '/' imgfiles(1).name], 'dir')
            imagefiles = dir([path fileName '/' videoname '/' imgfiles(1).name '/']);
            imagefiles = imagefiles(3:end);
            
            if size(imagefiles, 1) < 100, range_1_100 = range_1_100 + 1; end
            if size(imagefiles, 1) >= 100 && size(imagefiles, 1) < 300,  range_101_300 = range_101_300 + 1; end
            if size(imagefiles, 1) >= 300 && size(imagefiles, 1) < 500,  range_301_500 = range_301_500 + 1; end
            if size(imagefiles, 1) >= 500 && size(imagefiles, 1) < 700,  range_500_700 = range_500_700 + 1; end
            if size(imagefiles, 1) >= 700 && size(imagefiles, 1) < 1000, range_701_1000 = range_701_1000 + 1; end
            if size(imagefiles, 1) >= 1000, range_1000 = range_1000 + 1; end
            
            if iid == 1 && id == 12
                min_frames = size(imagefiles, 1);
                % mean_frames = size(imagefiles, 1);
                max_frames = size(imagefiles, 1);
                total_frame = total_frame + size(imagefiles, 1);
            else
                if min_frames > size(imagefiles, 1), min_frames = size(imagefiles, 1); end
                if max_frames < size(imagefiles, 1), max_frames = size(imagefiles, 1); end
                total_frame = total_frame + size(imagefiles, 1);
            end
        elseif exist([path fileName '/' videoname '/' imgfiles(2).name], 'dir')
            imagefiles = dir([path fileName '/' videoname '/' imgfiles(2).name '/']);
            imagefiles = imagefiles(3:end);
            
            if size(imagefiles, 1) < 100, range_1_100 = range_1_100 + 1; end
            if size(imagefiles, 1) >= 100 && size(imagefiles, 1) < 300,  range_101_300 = range_101_300 + 1; end
            if size(imagefiles, 1) >= 300 && size(imagefiles, 1) < 500,  range_301_500 = range_301_500 + 1; end
            if size(imagefiles, 1) >= 500 && size(imagefiles, 1) < 700,  range_500_700 = range_500_700 + 1; end
            if size(imagefiles, 1) >= 700 && size(imagefiles, 1) < 1000, range_701_1000 = range_701_1000 + 1; end
            if size(imagefiles, 1) >= 1000, range_1000 = range_1000 + 1; end
            
            if iid == 1 && id == 12
                min_frames = size(imagefiles, 1);
                % mean_frames = size(imagefiles, 1);
                max_frames = size(imagefiles, 1);
                total_frame = total_frame + size(imagefiles, 1);
            else
                if min_frames > size(imagefiles, 1), min_frames = size(imagefiles, 1); end
                if max_frames < size(imagefiles, 1), max_frames = size(imagefiles, 1); end
                total_frame = total_frame + size(imagefiles, 1);
            end

        elseif exist([path fileName '/' videoname '/' imgfiles(3).name], 'dir')
            imagefiles = dir([path fileName '/' videoname '/' imgfiles(3).name '/']);
            imagefiles = imagefiles(3:end);
            
            if size(imagefiles, 1) < 100, range_1_100 = range_1_100 + 1; end
            if size(imagefiles, 1) >= 100 && size(imagefiles, 1) < 300,  range_101_300 = range_101_300 + 1; end
            if size(imagefiles, 1) >= 300 && size(imagefiles, 1) < 500,  range_301_500 = range_301_500 + 1; end
            if size(imagefiles, 1) >= 500 && size(imagefiles, 1) < 700,  range_500_700 = range_500_700 + 1; end
            if size(imagefiles, 1) >= 700 && size(imagefiles, 1) < 1000, range_701_1000 = range_701_1000 + 1; end
            if size(imagefiles, 1) >= 1000, range_1000 = range_1000 + 1; end
            
            if iid == 1 && id == 12
                min_frames = size(imagefiles, 1);
                % mean_frames = size(imagefiles, 1);
                max_frames = size(imagefiles, 1);
                total_frame = total_frame + size(imagefiles, 1);
            else
                if min_frames > size(imagefiles, 1), min_frames = size(imagefiles, 1); end
                if max_frames < size(imagefiles, 1), max_frames = size(imagefiles, 1); end
                total_frame = total_frame + size(imagefiles, 1);
            end

        elseif exist([path fileName '/' videoname '/' imgfiles(4).name], 'dir')
            imagefiles = dir([path fileName '/' videoname '/' imgfiles(4).name '/']);
            imagefiles = imagefiles(3:end);
            
            if size(imagefiles, 1) < 100, range_1_100 = range_1_100 + 1; end
            if size(imagefiles, 1) >= 100 && size(imagefiles, 1) < 300,  range_101_300 = range_101_300 + 1; end
            if size(imagefiles, 1) >= 300 && size(imagefiles, 1) < 500,  range_301_500 = range_301_500 + 1; end
            if size(imagefiles, 1) >= 500 && size(imagefiles, 1) < 700,  range_500_700 = range_500_700 + 1; end
            if size(imagefiles, 1) >= 700 && size(imagefiles, 1) < 1000, range_701_1000 = range_701_1000 + 1; end
            if size(imagefiles, 1) >= 1000, range_1000 = range_1000 + 1; end
            
            if iid == 1 && id == 12
                min_frames = size(imagefiles, 1);
                % mean_frames = size(imagefiles, 1);
                max_frames = size(imagefiles, 1);
                total_frame = total_frame + size(imagefiles, 1);
            else
                if min_frames > size(imagefiles, 1), min_frames = size(imagefiles, 1); end
                if max_frames < size(imagefiles, 1), max_frames = size(imagefiles, 1); end
                total_frame = total_frame + size(imagefiles, 1);
            end

        end 
        
%         if min_frames == 2
%             break; 
%         end 
            
    end
    
end

 
mean_frames = total_frame / videoNUM;





%% 
% min_frames  =  18 
% mean_frames =  450 
% max_frames  =  6246 
% total_frame =  371128 
% 
% 
% 1, 100      = 276 
% 101, 300    = 222 
% 301, 500    = 76 
% 501, 700    = 65 
% 701, 1000   = 75 
% 1000        = 111 



y=[276; 222; 76;  65;  75;  111;];
b=bar(y);
grid on;
ch = get(b,'children');
set(gca,'XTickLabel',{'1-100','101-300','301-500','501-700','701-1000','1000+'})
% set(ch,'FaceVertexCData',[1 0 1;0 0 0;])
% legend('基于XXX的算法','基于YYY的算法');
% xlabel('x axis ');
% ylabel('y axis');



















































