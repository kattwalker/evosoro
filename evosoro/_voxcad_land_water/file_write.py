
import hashlib
import os
import time
import random


#This class(??) does the writing of the vxa file that will be read by voxelyze and used in the testing!
#  I think at some point I will have to work out how to put in indiviual bitsof the phenotype in, but we'll leave it for the moment.  

def write_voxelyze_file(t,morphology):

    
    t=str(t)
    morphology_l1=str(morphology[0])
    morphology_l1=morphology_l1.replace(',','')
    morphology_l1=morphology_l1.replace(" ", "")
    morphology_l2=str(morphology[1])
    morphology_l2 = morphology_l2.replace(',','')
    morphology_l2=morphology_l2.replace(" ", "")
    morphology_l3=str(morphology[2])
    morphology_l3 = morphology_l3.replace(',','')
    morphology_l3=morphology_l3.replace(" ", "")
    morphology_l4=str(morphology[3])
    morphology_l4 = morphology_l4.replace(',','')
    morphology_l4=morphology_l4.replace(" ", "")
    morphology_l5=str(morphology[4])
    morphology_l5 = morphology_l5.replace(',','')
    morphology_l5=morphology_l5.replace(" ", "")
    morphology_l6=str(morphology[5])
    morphology_l6 = morphology_l6.replace(',','')
    morphology_l6=morphology_l6.replace(" ", "")
    morphology_l7=str(morphology[6])
    morphology_l7 = morphology_l7.replace(',','')
    morphology_l7=morphology_l7.replace(" ", "")

    #first we need to open the file, for writing purposes
    voxelyze_file = open("katt"+t+".vxa", "w")

    #then this is the actual writing bit
    voxelyze_file.write(
    "<?xml version=\"1.0\" encoding=\"ISO-8859-1\"?>\n\
    <VXA Version=\"1.0\">\n\
    <Simulator>\n\
    <Integration>\n\
    <Integrator>0</Integrator>\n\
    <DtFrac>0.9</DtFrac>\n\
    </Integration>\n\
    <Damping>\n\
    <BondDampingZ>1</BondDampingZ>\n\
    <ColDampingZ>0.8</ColDampingZ>\n\
    <SlowDampingZ>0.01</SlowDampingZ>\n\
    </Damping>\n\
    <Collisions>\n\
    <SelfColEnabled>1</SelfColEnabled>\n\
    <ColSystem>3</ColSystem>\n\
    <CollisionHorizon>2</CollisionHorizon>\n\
    </Collisions>\n\
    <Features>\n\
    <FluidDampEnabled>0</FluidDampEnabled>\n\
    <PoissonKickBackEnabled>0</PoissonKickBackEnabled>\n\
    <EnforceLatticeEnabled>0</EnforceLatticeEnabled>\n\
    </Features>\n\
    <SurfMesh>\n\
    <CMesh>\n\
    <DrawSmooth>1</DrawSmooth>\n\
    <Vertices/>\n\
    <Facets/>\n\
    <Lines/>\n\
    </CMesh>\n\
    </SurfMesh>\n\
    <StopCondition>\n\
    <StopConditionType>2</StopConditionType>\n\
    <StopConditionValue>5</StopConditionValue>\n\
    <InitCmTime>0.0</InitCmTime>\n\
    </StopCondition>\n\
    <GA>\n\
    <WriteFitnessFile>1</WriteFitnessFile>\n\
    <FitnessFileName>my_fitness"+t+".xml</FitnessFileName>\n\
    <QhullTmpFile>Qhull_temp"+t+"</QhullTmpFile>\n\
    <CurvaturesTmpFile>curve_temp"+t+"</CurvaturesTmpFile>\n\
    </GA>\n\
    </Simulator>\n\
    <Environment>\n\
    <Fixed_Regions>\n\
    <NumFixed>0</NumFixed>\n\
    </Fixed_Regions>\n\
    <Forced_Regions>\n\
    <NumForced>0</NumForced>\n\
    </Forced_Regions>\n\
    <Gravity>\n\
    <GravEnabled>1</GravEnabled>\n\
    <GravAcc>-9.81</GravAcc>\n\
    <FloorEnabled>1</FloorEnabled>\n\
    <FloorSlope>0.0</FloorSlope>\n\
    </Gravity>\n\
    <Thermal>\n\
    <TempEnabled>1</TempEnabled>\n\
    <TempAmp>39</TempAmp>\n\
    <TempBase>25</TempBase>\n\
    <VaryTempEnabled>1</VaryTempEnabled>\n\
    <TempPeriod>0.263662540539</TempPeriod>\n\
    </Thermal>\n\
    </Environment>\n\
    <VXC Version=\"0.93\">\n\
    <Lattice>\n\
    <Lattice_Dim>0.05</Lattice_Dim>\n\
    <X_Dim_Adj>1</X_Dim_Adj>\n\
    <Y_Dim_Adj>1</Y_Dim_Adj>\n\
    <Z_Dim_Adj>1</Z_Dim_Adj>\n\
    <X_Line_Offset>0</X_Line_Offset>\n\
    <Y_Line_Offset>0</Y_Line_Offset>\n\
    <X_Layer_Offset>0</X_Layer_Offset>\n\
    <Y_Layer_Offset>0</Y_Layer_Offset>\n\
    </Lattice>\n\
    <Voxel>\n\
    <Vox_Name>BOX</Vox_Name>\n\
    <X_Squeeze>1</X_Squeeze>\n\
    <Y_Squeeze>1</Y_Squeeze>\n\
    <Z_Squeeze>1</Z_Squeeze>\n\
    </Voxel>\n\
    <Palette>\n\
    <Material ID=\"1\">\n\
    <MatType>0</MatType>\n\
    <Name>Passive_Soft</Name>\n\
    <Display>\n\
    <Red>0</Red>\n\
    <Green>1</Green>\n\
    <Blue>1</Blue>\n\
    <Alpha>1</Alpha>\n\
    </Display>\n\
    <Mechanical>\n\
    <MatModel>0</MatModel>\n\
    <Elastic_Mod>1.0e+006</Elastic_Mod>\n\
    <Plastic_Mod>0</Plastic_Mod>\n\
    <Yield_Stress>0</Yield_Stress>\n\
    <FailModel>0</FailModel>\n\
    <Fail_Stress>0</Fail_Stress>\n\
    <Fail_Strain>0</Fail_Strain>\n\
    <Density>1200.0</Density>\n\
    <Poissons_Ratio>0.4</Poissons_Ratio>\n\
    <CTE>0</CTE>\n\
    <uStatic>1</uStatic>\n\
    <uDynamic>0.5</uDynamic>\n\
    </Mechanical>\n\
    </Material>\n\
    <Material ID=\"2\">\n\
    <MatType>0</MatType>\n\
    <Name>Passive_Hard</Name>\n\
    <Display>\n\
    <Red>0</Red>\n\
    <Green>0</Green>\n\
    <Blue>1</Blue>\n\
    <Alpha>1</Alpha>\n\
    </Display>\n\
    <Mechanical>\n\
    <MatModel>0</MatModel>\n\
    <Elastic_Mod>1.0e+008</Elastic_Mod>\n\
    <Plastic_Mod>0</Plastic_Mod>\n\
    <Yield_Stress>0</Yield_Stress>\n\
    <FailModel>0</FailModel>\n\
    <Fail_Stress>0</Fail_Stress>\n\
    <Fail_Strain>0</Fail_Strain>\n\
    <Density>1200.0</Density>\n\
    <Poissons_Ratio>0.4</Poissons_Ratio>\n\
    <CTE>0</CTE>\n\
    <uStatic>1</uStatic>\n\
    <uDynamic>0.5</uDynamic>\n\
    </Mechanical>\n\
    </Material>\n\
    <Material ID=\"3\">\n\
    <MatType>0</MatType>\n\
    <Name>Active_+</Name>\n\
    <Display>\n\
    <Red>1</Red>\n\
    <Green>0</Green>\n\
    <Blue>0</Blue>\n\
    <Alpha>1</Alpha>\n\
    </Display>\n\
    <Mechanical>\n\
    <MatModel>0</MatModel>\n\
    <Elastic_Mod>1.0e+006</Elastic_Mod>\n\
    <Plastic_Mod>0</Plastic_Mod>\n\
    <Yield_Stress>0</Yield_Stress>\n\
    <FailModel>0</FailModel>\n\
    <Fail_Stress>0</Fail_Stress>\n\
    <Fail_Strain>0</Fail_Strain>\n\
    <Density>1200.0</Density>\n\
    <Poissons_Ratio>0.4</Poissons_Ratio>\n\
    <CTE>0.01</CTE>\n\
    <uStatic>1</uStatic>\n\
    <uDynamic>0.5</uDynamic>\n\
    </Mechanical>\n\
    </Material>\n\
    <Material ID=\"4\">\n\
    <MatType>0</MatType>\n\
    <Name>Active_-</Name>\n\
    <Display>\n\
    <Red>0</Red>\n\
    <Green>1</Green>\n\
    <Blue>0</Blue>\n\
    <Alpha>1</Alpha>\n\
    </Display>\n\
    <Mechanical>\n\
    <MatModel>0</MatModel>\n\
    <Elastic_Mod>1.0e+006</Elastic_Mod>\n\
    <Plastic_Mod>0</Plastic_Mod>\n\
    <Yield_Stress>0</Yield_Stress>\n\
    <FailModel>0</FailModel>\n\
    <Fail_Stress>0</Fail_Stress>\n\
    <Fail_Strain>0</Fail_Strain>\n\
    <Density>1200.0</Density>\n\
    <Poissons_Ratio>0.4</Poissons_Ratio>\n\
    <CTE>-0.01</CTE>\n\
    <uStatic>1</uStatic>\n\
    <uDynamic>0.5</uDynamic>\n\
    </Mechanical>\n\
    </Material>\n\
    <Material ID=\"5\">\n\
    <MatType>0</MatType>\n\
    <Name>Aperture</Name>\n\
    <Display>\n\
    <Red>1</Red>\n\
    <Green>0.784</Green>\n\
    <Blue>0</Blue>\n\
    <Alpha>1</Alpha>\n\
    </Display>\n\
    <Mechanical>\n\
    <MatModel>0</MatModel>\n\
    <Elastic_Mod>5e+007</Elastic_Mod>\n\
    <Plastic_Mod>0</Plastic_Mod>\n\
    <Yield_Stress>0</Yield_Stress>\n\
    <FailModel>0</FailModel>\n\
    <Fail_Stress>0</Fail_Stress>\n\
    <Fail_Strain>0</Fail_Strain>\n\
    <Density>1200.0</Density>\n\
    <Poissons_Ratio>0.4</Poissons_Ratio>\n\
    <CTE>0</CTE>\n\
    <uStatic>1</uStatic>\n\
    <uDynamic>0.5</uDynamic>\n\
    </Mechanical>\n\
    </Material>\n\
    </Palette>\n\
    <Structure Compression=\"ASCII_READABLE\">\n\
    <X_Voxels>7</X_Voxels>\n\
    <Y_Voxels>7</Y_Voxels>\n\
    <Z_Voxels>7</Z_Voxels>\n\
    <Data>\n\
    <Layer><![CDATA"+morphology_l1+"]></Layer>\n\
    <Layer><![CDATA"+morphology_l2+"]></Layer>\n\
    <Layer><![CDATA"+morphology_l3+"]></Layer>\n\
    <Layer><![CDATA"+morphology_l4+"]></Layer>\n\
    <Layer><![CDATA"+morphology_l5+"]></Layer>\n\
    <Layer><![CDATA"+morphology_l6+"]></Layer>\n\
    <Layer><![CDATA"+morphology_l7+"]></Layer>\n\
    </Data>\n\
    <PhaseOffset>\n\
    <Layer><![CDATA[0.1, -0, -0, -0, -0.1, -0, 0.1, -0, -0.16, -0.2, -0.2, -0.2, -0.16, -0, -0.1, -0.2, -0.35, -0.38, -0.34, -0.25, -0.1, -0.13, -0.28, -0.38, -0.41, -0.38, -0.28, -0.13, -0.10, -0.25, -0.35, -0.38, -0.35, -0.25, -0.11, -0, -0.16, -0.25, -0.29, -0.25, -0.16, -0.0, 0.0, -0.0, -0.11, -0.14, -0.11 -0.02, 0, ]]></Layer>\n\
    <Layer><![CDATA[0.1, 0, -0, -0.1, -0.0, 0, 0.1, 0, -0.18, -0.2, -0.3, -0.2, -0.1, 0, -0.0, -0.2, -0.3, -0.4, -0.3, -0.2, -0.0, -0.1, -0.3, -0.4, -0.4, -0.4, -0.3, -0.1, -0.1, -0.2, -0.3, -0.4, -0.40, -0.2, -0.1, -0, -0.17, -0.2, -0.3, -0.2, -0.17, -0, 0.13, -0.0, -0.1, -0.13, -0.1, -0, 0.13, ]]></Layer>\n\
    <Layer><![CDATA[0.2, 0, 0, 0, 0, 0, 0, 0, -0.11, -0.2, -0.2, -0.2, -0.1, 0, -0, -0.2, -0.3, -0.4, -0.3, -0.2, -0, -0, -0.2, -0.4, -0.4, -0.4, -0.2, -0, -0, -0.2, -0.3, -0.4, -0.3, -0.2, -0, 0, -0.1, -0.2, -0.2, -0.2, -0.1, 0, 0.2, 0, -0, -0, -0, 0, 0.2 ]]></Layer>\n\
    <Layer><![CDATA[0.3, 0.2, 0, 0, 0, 0.2, 0.3, 0.2, 0, -0.1, -0.1, -0.1, 0, 0.2, 0, -0.1, -0.2, -0.3, -0.2, -0.1, 0, 0, -0.1, -0.3, -0.4, -0.3, -0.1, 0, 0, -0.1, -0.2, -0.3, -0.2, -0.1, 0, 0.1, 0, -0.1, -0.1, -0.1, -0, 0.1, 0.3, 0.1, 0, 0, 0, 0, 0.3, ]]></Layer>\n\
    <Layer><![CDATA[0.5, 0.3, 0.2, 0.2, 0.3, 0.3, 0.5, 0.3, 0.2, 0, 0, 0, 0.2, 0.3, 0.2, 0.1, 0, 0, -0, 0, 0.2, 0.2, 0, -0, -0.1, -0.1, 0, 0.2, 0.2, 0.1, 0, -0.1, -0, 0, 0.2, 0.3, 0.2, 0, 0, 0, 0.2, 0.3, 0.5, 0.3, 0.2, 0.2, 0.2, 0.3, 0.5 ]]></Layer>\n\
    <Layer><![CDATA[0.6, 0.6, 0.5, 0.5, 0.5, 0.6, 0.6, 0.6, 0.4, 0.3, 0.3, 0.3, 0.4, 0.6, 0.5, 0.3, 0.2, 0.2, 0.2, 0.3, 0.5, 0.5, 0.3, 0.2, 0.1, 0.2, 0.3, 0.5, 0.5, 0.3, 0.2, 0.2, 0.2, 0.3, 0.5, 0.5, 0.4, 0.3, 0.3, 0.3, 0.4, 0.5, 0.6, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6 ]]></Layer>\n\
    <Layer><![CDATA[0.8, 0.7, 0.7, 0.7, 0.7, 0.7, 0.8, 0.7, 0.7, 0.6, 0.6, 0.6, 0.7, 0.7, 0.7, 0.6, 0.5, 0.5, 0.5, 0.6, 0.7, 0.7, 0.6, 0.5, 0.5, 0.5, 0.6, 0.7, 0.7, 0.6, 0.5, 0.5, 0.5, 0.6, 0.7, 0.7, 0.7, 0.6, 0.6, 0.6, 0.7, 0.7, 0.8, 0.7, 0.7, 0.7, 0.7, 0.7, 0.8 ]]></Layer>\n\
    </PhaseOffset>\n\
    </Structure>\n\
    </VXC>\n\
    </VXA>")
    voxelyze_file.close()
    return

def read_voxelyze_file(ta):
    this_file=open("my_fitness"+ta+".xml")
    tag="<normDistX>"
    results=0
    for line in this_file:
                if tag in line:
                    results = float(line[line.find(tag) + len(tag):line.find("</" + tag[1:])])
                    results=round(results,4)
    this_file.close()
   
    return results  
  
