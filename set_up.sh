function dlroot_create_and_write_file(){
    local content=$1
    local file_path=$2
    #dlroot_check_root_user

    if [[ $? -eq 0 ]]; then
        echo -e $content > $file_path
    else
        return
    fi
}

function set_pybase_env_path(){
    local content=`pwd`

    local file_dir=`python get_dir.py`
    local file_path="$file_dir/site-packages/pybase.pth"
    echo $file_path
    dlroot_create_and_write_file "$content" "$file_path"
}


set_pybase_env_path
