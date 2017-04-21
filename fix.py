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
