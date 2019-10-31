class parentClass(object):
    def parentClassMethod(self):
        print 'This Is parentClassMethod'


class childClass(parentClass):
    def callParentMethod(self):

        # FIRST arg - type from wheach begin search argument in parent
        super(childClass, self).parentClassMethod()
        # equal expression
        # parentClass.parentClassMethod(self)

child = childClass()
child.callParentMethod()
