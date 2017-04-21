env = Environment()

# begin fix
import SCons.Node.FS
def changed_fix( self, node=None, allowcache=False ):
   try:
      return self._memo['changed']
   except KeyError:
      pass

   has_changed = SCons.Node.Node.changed( self, node )
   if allowcache:
      self._memo['changed'] = has_changed
   return has_changed

SCons.Node.FS.File.changed = changed_fix
# end fix

#SConscript('SConscript-generate.py', exports='env', variant_dir='build/generator', duplicate=0)
import os
import shutil
if not os.path.exists('build'):
   os.makedirs('build')
if not os.path.exists('build/generator'):
   os.makedirs('build/generator')
shutil.copyfile('generator/SConscript-generate.py', 'build/generator/SConscript-generate.py')
VariantDir('build/generator', 'generator', duplicate=0)
SConscript('build/generator/SConscript-generate.py', exports='env')
SConscript('SConscript', exports='env', variant_dir='build/application', duplicate=0)
#SConscript('SConscript-generate.py', exports='env')
#SConscript('SConscript', exports='env')
