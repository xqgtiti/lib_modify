#把各个jar下的.class进行归并，用于proguard
def merge(apk_name, num):

    # 创建映射文件，后续重新分包时需要
    f_out = open(PROGUARD_WORK_SPACE_WIN +'dir_'+apk_name+'//map_out.txt', 'w')

    #归并的目录
    merge_dir_path_root = PROGUARD_WORK_SPACE_WIN +'dir_'+apk_name+'\\classes_merge\\'

    if os.path.exists(merge_dir_path_root) == False:
        os.makedirs(merge_dir_path_root)

    for i in range(1, num+1):
        if i == 1: num_s = ""
        else: num_s = str(i)

        jar_dir_path = PROGUARD_WORK_SPACE_WIN +'dir_'+apk_name+'\\classes%s-dex2jar'%num_s

        #先新建一个文件夹，用于之后划分，然后直接建好里面的目录
        split_dir_path = PROGUARD_WORK_SPACE_WIN +'dir_'+apk_name+'\\classes%s-split\\'%num_s
        if os.path.exists(split_dir_path) == False: os.makedirs(split_dir_path)

        for root, dirs, files in os.walk(jar_dir_path,'rb'):
            for dir in dirs:
                dir_inside = str(os.path.join(root[len(jar_dir_path ) + 1:], dir))
                merge_dir_path = merge_dir_path_root + dir_inside
                if os.path.exists(merge_dir_path) == False:
                    os.makedirs(merge_dir_path)
                if os.path.exists(split_dir_path + dir_inside) == False:
                    os.makedirs(split_dir_path + dir_inside)

            for file in files:
                filePath = str(os.path.join(root, file))
                file_inside = str(os.path.join(root[len(jar_dir_path) + 1:], file))
                merge_file_path = merge_dir_path_root + file_inside
                f_out.write(str(i) + '@@' + file_inside + '\n')
                if os.path.exists(merge_file_path) == False:
                    #print 'cp file:' + merge_file_path
                    shutil.copyfile(filePath, merge_file_path)