Import('env')

env.Command(['soapC.cpp'], None, './generator/generate.sh $TARGET')
