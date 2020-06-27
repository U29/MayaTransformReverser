def reversePose():
    import maya.cmds as cmds

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
        