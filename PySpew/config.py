import tomllib

with open ("../exampleconf.toml", "rb") as conf:
    config = tomllib.load(conf)

debug = config["DEBUG"]
disable_shell = config["DISABLE_SHELL"]
disable_print = config["DISABLE_PRINT"]
disable_mkdir = config["DISABLE_MKDIR"]
disable_file = config["DISABLE_FILE"]
disable_download = config["DISABLE_DOWNLOAD"]
disable_unzip  = config["DISABLE_UNZIP"]
disable_alias = config["DISABLE_ALIAS"]
disable_delete = config["DISABLE_DELETE"]
prompt_user_for_big_downloads = config["PROMPT_USER_FOR_BIG_DOWNLOADS"]
big_download_size_mb = config["BIG_DOWNLOAD_SIZE_MB"]
prompt_user_for_every_command = config["PROMPT_USER_FOR_EVERY_COMMAND"]
prompt_user_for_dangerous_commands = config["PROMPT_USER_FOR_DANGEROUS_COMMANDS"]
allowed_shell_commands = config["ALLOWED_SHELL_COMMANDS"]
blacklisted_shell_commands = config["BLACKLISTED_SHELL_COMMANDS"]
danger = config["IGNORE_ALL_SAFETY_MEASURES_INCLUDING_DISABLING_AND_SHELL_COMMAND_BLACKLISTING_VERY_DANGEROUS"]
log_file_path = config["LOG_FILE_PATH"]
max_log_file_size_mb = config["MAX_LOG_FILE_SIZE_MB"]
allow_executing_of_different_os_commands = config["ALLOW_EXECUTING_OF_DIFFERENT_OS_COMMANDS"]
unzip_backend_windows = config["UNZIP_BACKEND_WINDOWS"]
unzip_backend_osx = config["UNZIP_BACKEND_OSX"]
shell_used_on_linux = config["SHELL_USED_ON_LINUX"]
shell_used_on_osx = config["SHELL_USED_ON_OSX"]
shell_used_on_windows = config["SHELL_USED_ON_WINDOWS"]