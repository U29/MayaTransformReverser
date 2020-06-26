import maya.cmds as cmds
from maya.common.ui import LayoutManager

def testWindow():
    if cmds.window('ReverserWindow', ex=1):
        cmds.deleteUI('ReverserWindow')
    windowName = cmds.window('ReverserWindow',title='Transform Reverser BETA 0.01')
    tabTest = cmds.tabLayout(scrollable=False, innerMarginHeight=5, innerMarginWidth=1)
    with LayoutManager(cmds.columnLayout(adj=True, rowSpacing=10)) as tabTestColumn:
        with LayoutManager(cmds.rowLayout(numberOfColumns=4, columnAttach4=('left', 'left', 'left', 'left'), columnWidth4=(50, 50, 50, 50))):
            cmds.text(label="Translate")
            checkTx = cmds.checkBox('checkTx', label="X")
            checkTy = cmds.checkBox('checkTy',label="Y")
            checkTz = cmds.checkBox('checkTz',label="Z")
        with LayoutManager(cmds.rowLayout(numberOfColumns=4, columnAttach4=('left', 'left', 'left', 'left'), columnWidth4=(50, 50, 50, 50))):
            cmds.text(label="Rotate")
            cmds.checkBox('checkRx', label="X")
            cmds.checkBox('checkRy',label="Y")
            cmds.checkBox('checkRz',label="Z")
        with LayoutManager(cmds.rowLayout(numberOfColumns=4, columnAttach4=('left', 'left', 'left', 'left'), columnWidth4=(50, 50, 50, 50))):
            cmds.text(label="Scale")
            cmds.checkBox('checkSx', label="X")
            cmds.checkBox('checkSy',label="Y")
            cmds.checkBox('checkSz',label="Z")
        cmds.button(label="＼(^o^)／Reverse／(^o^)＼", command='reverse()')
        cmds.image( w=300 , h=300 , image = "D:/Downloads/83786474.jpeg" )
    cmds.tabLayout(tabTest, edit=1, tabLabel=(tabTestColumn, "Simple"))
    
    with LayoutManager(cmds.columnLayout(adj=True, rowSpacing=10)) as tabTestColumn2:
        with LayoutManager(cmds.rowLayout(numberOfColumns=4, columnAttach4=('left', 'left', 'left', 'left'), columnWidth4=(50, 50, 50, 50))):
            cmds.button(label="＼(^o^)／Reverse／(^o^)＼")
    cmds.tabLayout(tabTest, edit=2, tabLabel=(tabTestColumn2, "MoxRig"))
    
    cmds.showWindow()

if __name__ == '__main__':  
    testWindow()

def test():
    print bToS(cmds.checkBox('checkTz', q=True, value=True))
    
def reverse():
    checkTx = cmds.checkBox('checkTx', q=True, value=True)
    checkTy = cmds.checkBox('checkTy', q=True, value=True)
    checkTz = cmds.checkBox('checkTz', q=True, value=True)
    checkRx = cmds.checkBox('checkRx', q=True, value=True)
    checkRy = cmds.checkBox('checkRy', q=True, value=True)
    checkRz = cmds.checkBox('checkRz', q=True, value=True)
    checkSx = cmds.checkBox('checkSx', q=True, value=True)
    checkSy = cmds.checkBox('checkSy', q=True, value=True)
    checkSz = cmds.checkBox('checkSz', q=True, value=True)
    
    selected = cmds.ls(sl=True,long=True) or []
    
    # a loop which do something each objects 
    for eachSel in selected:
        eachSelT = cmds.getAttr(eachSel + '.translate')[0]
        eachSelR = cmds.getAttr(eachSel + '.rotate')[0]
        eachSelS = cmds.getAttr(eachSel + '.scale')[0]
        print eachSelT, eachSelR, eachSelS
        try:
            if 1:
                cmds.setAttr(eachSel + '.translate', bToS(checkTx)*eachSelT[0], bToS(checkTy)*eachSelT[1], bToS(checkTz)*eachSelT[2])
            if 1:
                cmds.setAttr(eachSel + '.rotate', bToS(checkRx)*eachSelR[0], bToS(checkRy)*eachSelR[1], bToS(checkRz)*eachSelR[2])
            if 0:
                cmds.setAttr(eachSel + '.scale', bToS(checkSx)*eachSelS[0], bToS(checkSy)*eachSelS[1], bToS(checkSz)*eachSelS[2])
        except:
            print "locked attributes didn't changed"            
def bToS(checked):
    if checked:
        return -1.0
    else:
        return 1.0