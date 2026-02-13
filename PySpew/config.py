import tomllib

flags = {}
validflags = ["disable_print","disable_shell","disable_mkdir","disable_file","disable_download","disable_unzip","disable_alias","disable_delete","print_if_command_disabled","prompt_user_for_big_downloads","big_download_size_mb","prompt_user_for_every_command","prompt_user_for_dangerous_commands","allowed_shell_commands","blacklisted_shell_commands","ignore_all_safety_measures_including_disabling_and_shell_command_blacklisting_very_dangerous","log_file_path","max_log_file_size_mb","allow_executing_of_different_os_commands","debug","unzip_backend_windows","unzip_backend_linux","unzip_backend_osx","shell_used_on_linux","shell_used_on_osx","shell_used_on_windows"]
with open ("./config/config.toml", "rb") as conf:
    config = tomllib.load(conf)
for key, value in config.items():
    lower_key = key.lower()
    if value == True:
        value = 1
    elif value == False:
        value = 0
    flags[lower_key] = value

def check_flags(string):
    for word in string.split():
        w = word.lower()
        if not word.lower().endswith(".spw") or word.lower().endswith(".spew"):
            if any(word.lower().startswith(prefix) for prefix in validflags) and "=" in w:
                parts = w.split("=", 1)
                key = parts[0]
                val = parts[1]
                flags[key] = int(val)