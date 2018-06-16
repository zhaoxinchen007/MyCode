
import maya.cmds as mc

AllSets=['Root_MoCap_M','Hip_MoCap_R','Knee_MoCap_R','Ankle_MoCap_R','Spine1_MoCap_M','Chest_MoCap_M','Neck_MoCap_M','Head_MoCap_M','Scapula_MoCap_R','Shoulder_MoCap_R',
'Elbow_MoCap_R','Wrist_MoCap_R','Scapula_MoCap_L','Shoulder_MoCap_L','Elbow_MoCap_L','Wrist_MoCap_L','Hip_MoCap_L','Knee_MoCap_L','Ankle_MoCap_L']

CtrlSets=['RootX_M','FKHip_L','FKKnee_L','FKAnkle_L','FKHip_R','FKKnee_R','FKAnkle_R','FKSpine1_M','FKChest_M','FKNeck_M','FKHead_M','FKScapula_L','FKShoulder_L','FKElbow_L','FKWrist_L',
'FKScapula_R','FKShoulder_R','FKElbow_R','FKWrist_R','IKArm_L','PoleArm_L','IKArm_R','PoleArm_R','IKLeg_L','IKLeg_R','PoleLeg_L','PoleLeg_R']

sn=mc.listConnections('Root_MoCap_M',type='animCurveTL')[0]
kt=mc.keyframe(sn,tc=1,q=1)

sels=mc.ls(sl=1)
nameS=sels[0].split(':')[0]
mc.currentTime('-100')
for AllSet in AllSets:
    mc.setAttr(AllSet+'.rotateX',0)
    mc.setAttr(AllSet+'.rotateY',0)
    mc.setAttr(AllSet+'.rotateZ',0)

mc.setAttr(AllSets[0]+'.translateX',0)
mc.setAttr(AllSets[0]+'.translateY',0)
mc.setAttr(AllSets[0]+'.translateZ',0)

mc.select('MoCap',hi=1)
ll=mc.ls(sl=1)
mc.setKeyframe(ll,t='1')

LocA=mc.spaceLocator(n='L_Arm_IkP')
LocB=mc.spaceLocator(n='R_Arm_IkP')
LocC=mc.spaceLocator(n='L_Leg_IkP')
LocD=mc.spaceLocator(n='R_Leg_IkP')

conL=mc.parentConstraint(nameS+':PoleArm_L',LocA,mo=0)
mc.delete(conL)
conL=mc.parentConstraint(nameS+':PoleArm_R',LocB,mo=0)
mc.delete(conL)
conL=mc.parentConstraint(nameS+':PoleLeg_L',LocC,mo=0)
mc.delete(conL)
conL=mc.parentConstraint(nameS+':PoleLeg_R',LocD,mo=0)
mc.delete(conL)

mc.parent(LocA,'Elbow_MoCap_L')
mc.parent(LocB,'Elbow_MoCap_R')
mc.parent(LocC,'Knee_MoCap_L')
mc.parent(LocD,'Knee_MoCap_R')

mc.pointConstraint(LocA,nameS+':PoleArm_L',mo=1)
mc.pointConstraint(LocB,nameS+':PoleArm_R',mo=1)
mc.pointConstraint(LocC,nameS+':PoleLeg_L',mo=1)
mc.pointConstraint(LocD,nameS+':PoleLeg_R',mo=1)
mc.parentConstraint('Root_MoCap_M',nameS+':RootX_M',mo=1)
mc.parentConstraint('Wrist_MoCap_L',nameS+':IKArm_L',mo=1)
mc.parentConstraint('Wrist_MoCap_R',nameS+':IKArm_R',mo=1)
mc.parentConstraint('Ankle_MoCap_L',nameS+':IKLeg_L',mo=1)
mc.parentConstraint('Ankle_MoCap_R',nameS+':IKLeg_R',mo=1)

for AllSet in AllSets[1:]:
    for CtrlSet in CtrlSets[1:]:
        if AllSet.replace('_MoCap','') in CtrlSet:
            mc.parentConstraint(AllSet,nameS+':'+CtrlSet,mo=1)