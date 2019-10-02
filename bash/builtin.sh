#The Shopt Builtin
# This builtin allows you to change additional shell optional behavior.
# If dotglob set, 
# Bash includes filenames beginning with a ‘.’ in the results of filename expansion. 
# The filenames ‘.’ and ‘..’ must always be matched explicitly, even if dotglob is set.
# Here we need dotglob to move all files(include hidden files) within the AT/ folder.
shopt -s dotglob && mv AT/* .
