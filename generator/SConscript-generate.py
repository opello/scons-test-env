Import('env')

def run_command(target, source, env):
   import subprocess
   subprocess.call(args=['./generate.sh', str(target[0])], shell=False, close_fds=True)
   #subprocess.call('./generate.sh {}'.format(target[0]), shell=False, close_fds=True)

action = env.Action(run_command)
#env.Command(['soapC.cpp'], None, action)
env.Command(['soapC.cpp'], None, './generator/generate.sh $TARGET')
