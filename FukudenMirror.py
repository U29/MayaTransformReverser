# -*- coding: utf-8 -*-
import maya.cmds as cmds
from maya.common.ui import LayoutManager

def bToS(checked):
    if checked:
        return -1.0
    else:
        return 1.0
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
        isLockedTx = cmds.getAttr(eachSel + '.tx', lock=True)
        isLockedTy = cmds.getAttr(eachSel + '.ty', lock=True)
        isLockedTz = cmds.getAttr(eachSel + '.tz', lock=True)
        isLockedRx = cmds.getAttr(eachSel + '.rx', lock=True)
        isLockedRy = cmds.getAttr(eachSel + '.ry', lock=True)
        isLockedRz = cmds.getAttr(eachSel + '.rz', lock=True)
        isLockedSx = cmds.getAttr(eachSel + '.sx', lock=True)
        isLockedSy = cmds.getAttr(eachSel + '.sy', lock=True)
        isLockedSz = cmds.getAttr(eachSel + '.sz', lock=True)
        
        print eachSelT, eachSelR, eachSelS
        try:
            if 1:
                if not isLockedTx:
                    cmds.setAttr(eachSel + '.tx', bToS(checkTx)*eachSelT[0])
                if not isLockedTy:
                    cmds.setAttr(eachSel + '.ty', bToS(checkTy)*eachSelT[1])
                if not isLockedTz:
                    cmds.setAttr(eachSel + '.tz', bToS(checkTz)*eachSelT[2])
            if 1:
                if not isLockedRx:
                    cmds.setAttr(eachSel + '.rx', bToS(checkRx)*eachSelR[0])
                if not isLockedRy:
                    cmds.setAttr(eachSel + '.ry', bToS(checkRy)*eachSelR[1])
                if not isLockedRz:
                    cmds.setAttr(eachSel + '.rz', bToS(checkRz)*eachSelR[2])
            if 1:
                if not isLockedSx:
                    cmds.setAttr(eachSel + '.rx', bToS(checkSx)*eachSelS[0])
                if not isLockedSy:
                    cmds.setAttr(eachSel + '.ry', bToS(checkSy)*eachSelS[1])
                if not isLockedSz:
                    cmds.setAttr(eachSel + '.rz', bToS(checkSz)*eachSelS[2])
        except:
            print "locked attributes didn't change"            
def mirrorPose():
    head = 'rig_Head'
    chest = 'rig_Spine1'
    waist = 'rig_Spine'
    shoulderL = 'rig_LeftShoulder'
    shoulderR = 'rig_RightShoulder'
    handL = 'rig_LeftHand'
    handR = 'rig_RightHand'
    elbowL = 'rig_LeftArmUpv'
    elbowR = 'rig_RightArmUpv'
    root = 'rig_COG'
    hip = 'rig_Hips'
    kneeL = 'rig_LeftLegUpv'
    kneeR = 'rig_RightLegUpv'
    footL = 'rig_LeftFoot'
    footR = 'rig_RightFoot'
    toeL = 'rig_LeftToeBase'
    toeR = 'rig_RightToeBase'

    # temps of hands
    tempHandL_T = cmds.getAttr(handL + '.translate')[0]
    tempHandL_R = cmds.getAttr(handL + '.rotate')[0]
    tempHandR_T = cmds.getAttr(handR + '.translate')[0]
    tempHandR_R = cmds.getAttr(handR + '.rotate')[0]
    # temps of elbows
    tempElbowL_T = cmds.getAttr(elbowL + '.translate')[0]
    tempElbowR_T = cmds.getAttr(elbowR + '.translate')[0]
    # temps of shoulders
    tempShoulderL_R = cmds.getAttr(shoulderL + '.rotate')[0]
    tempShoulderR_R = cmds.getAttr(shoulderR + '.rotate')[0]
    # temps of knees
    tempKneeL_T = cmds.getAttr(kneeL + '.translate')[0]
    tempKneeR_T = cmds.getAttr(kneeR + '.translate')[0]
    # temps of foots
    tempFootL_T = cmds.getAttr(footL + '.translate')[0]
    tempFootL_R = cmds.getAttr(footL + '.rotate')[0]
    tempFootR_T = cmds.getAttr(footR + '.translate')[0]
    tempFootR_R = cmds.getAttr(footR + '.rotate')[0]
    # temps of toes
    tempToeL_R = cmds.getAttr(toeL + '.rotate')[0]
    tempToeR_R = cmds.getAttr(toeR + '.rotate')[0]

    selected = cmds.ls(sl=True) or []


    for eachObj in selected:
        tempTx = cmds.getAttr(eachObj + '.tx')
        tempTy = cmds.getAttr(eachObj + '.ty')
        tempTz = cmds.getAttr(eachObj + '.tz')
        tempRx = cmds.getAttr(eachObj + '.rx')
        tempRy = cmds.getAttr(eachObj + '.ry')
        tempRz = cmds.getAttr(eachObj + '.rz')

        if eachObj == head or eachObj == chest or eachObj == waist or eachObj == hip:
            cmds.setAttr(eachObj + '.ry', -tempRy)
            cmds.setAttr(eachObj + '.rz', -tempRz)
        elif eachObj == root:
            cmds.setAttr(eachObj + '.tx', -tempTx) # maybe
            cmds.setAttr(eachObj + '.ry', -tempRy)
            cmds.setAttr(eachObj + '.rz', -tempRz)
        
        elif eachObj == handL:
            cmds.setAttr(eachObj + '.translate', -tempHandR_T[0], tempHandR_T[1], tempHandR_T[2])
            cmds.setAttr(eachObj + '.rotate', tempHandR_R[0], -tempHandR_R[1], -tempHandR_R[2])
        elif eachObj == handR:
            cmds.setAttr(eachObj + '.translate', -tempHandL_T[0], tempHandL_T[1], tempHandL_T[2])
            cmds.setAttr(eachObj + '.rotate', tempHandL_R[0], -tempHandL_R[1], -tempHandL_R[2])
        elif eachObj == elbowL:
            cmds.setAttr(eachObj + '.translate', -tempElbowR_T[0], tempElbowR_T[1], -tempElbowR_T[2])
        elif eachObj == elbowR:
            cmds.setAttr(eachObj + '.translate', -tempElbowL_T[0], tempElbowL_T[1], -tempElbowL_T[2])
        elif eachObj == shoulderL:
            cmds.setAttr(eachObj + '.rotate', tempShoulderR_R[0], -tempShoulderR_R[1], -tempShoulderR_R[2])
        elif eachObj == shoulderR:
            cmds.setAttr(eachObj + '.rotate', tempShoulderL_R[0], -tempShoulderL_R[1], -tempShoulderL_R[2])
        elif eachObj == kneeL:
            cmds.setAttr(eachObj + '.translate', -tempKneeR_T[0], tempKneeR_T[1], tempKneeR_T[2])
        elif eachObj == kneeR:
            cmds.setAttr(eachObj + '.translate', -tempKneeL_T[0], tempKneeL_T[1], tempKneeL_T[2])
        elif eachObj == footL:
            cmds.setAttr(eachObj + '.translate', -tempFootR_T[0], tempFootR_T[1], tempFootR_T[2])
            cmds.setAttr(eachObj + '.rotate', tempFootR_R[0], -tempFootR_R[1], -tempFootR_R[2])
        elif eachObj == footR:
            cmds.setAttr(eachObj + '.translate', -tempFootL_T[0], tempFootL_T[1], tempFootL_T[2])
            cmds.setAttr(eachObj + '.rotate', tempFootL_R[0], -tempFootL_R[1], -tempFootL_R[2])
        elif eachObj == toeL:
            cmds.setAttr(eachObj + '.rotate', tempToeR_R[0], tempToeR_R[1], -tempToeR_R[2])
        elif eachObj == toeR:
            cmds.setAttr(eachObj + '.rotate', tempToeL_R[0], tempToeL_R[1], -tempToeL_R[2])
        
def mainWindow():
    if cmds.window('ReverserWindow', ex=1):
        cmds.deleteUI('ReverserWindow')
    windowName = cmds.window('ReverserWindow',title='Fukuden Mirror v0.01')
    tabTest = cmds.tabLayout(scrollable=False, innerMarginHeight=5, innerMarginWidth=1)
    
    with LayoutManager(cmds.columnLayout(adj=True, rowSpacing=10)) as tabTestColumn2:
        cmds.button(label="(^o MirrorPose o^)", command='FukudenMirror.mirrorPose()')
        cmds.tabLayout(tabTest, edit=1, tabLabel=(tabTestColumn2, "MirrorPose"))

    with LayoutManager(cmds.columnLayout(adj=True, rowSpacing=10)) as tabTestColumn:
        with LayoutManager(cmds.rowLayout(numberOfColumns=4, columnAttach4=('right', 'left', 'left', 'left'), columnWidth4=(50, 50, 50, 50))):
            cmds.text(label="Translate")
            checkTx = cmds.checkBox('checkTx', label="X")
            checkTy = cmds.checkBox('checkTy',label="Y")
            checkTz = cmds.checkBox('checkTz',label="Z")
        with LayoutManager(cmds.rowLayout(numberOfColumns=4, columnAttach4=('right', 'left', 'left', 'left'), columnWidth4=(50, 50, 50, 50))):
            cmds.text(label="Rotate")
            cmds.checkBox('checkRx', label="X")
            cmds.checkBox('checkRy',label="Y")
            cmds.checkBox('checkRz',label="Z")
        with LayoutManager(cmds.rowLayout(numberOfColumns=4, columnAttach4=('right', 'left', 'left', 'left'), columnWidth4=(50, 50, 50, 50))):
            cmds.text(label="Scale")
            cmds.checkBox('checkSx', label="X")
            cmds.checkBox('checkSy',label="Y")
            cmds.checkBox('checkSz',label="Z")
        cmds.button(label="(-o-)Reverse(_o_)", command='FukudenMirror.reverse()')
    cmds.tabLayout(tabTest, edit=2, tabLabel=(tabTestColumn, "ReversePSR"))
    
    cmds.showWindow()

if __name__ == '__main__':
    mainWindow()
