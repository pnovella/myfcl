from subprocess import call

run ="3350" 

srun = "000"

tfile = "dstbuilder.fcl"

ipath = "/lustre/neu/data4/DEMO_RUNNES/%s/"%run 

opath = "/data4/NEXT/users/pnovella/DATA/" 

idata = "run_%s.gdc1.%s.next1el"%(run,srun)

label = "DST_%s_%s"%(run,srun)

odata = label+".root"

jfile = "dstbuilder_%s.fcl"%label

sfile = jfile+".sub"

############################################

subcmd = """
#PBS -N job_%s
#PBS -q short
###PBS -M pau.novella@ific.uv.es
#PBS -e /data4/NEXT/users/pnovella/jobs/logs/%s.err
#PBS -o /data4/NEXT/users/pnovella/jobs/logs/%s.out
#PBS -m bae

source /home/pnovella/NEXT/NEXTREL/setup.sh

art -c /data4/NEXT/users/pnovella/jobs/fcl/%s
"""%(label,label,label,jfile)

tf = open(tfile,"read")

jf = open(jfile,"write")

for line in tf.readlines(): 
    
    line = line.replace("INPUT_DATA",ipath+idata)

    line = line.replace("OUTPUT_DATA",opath+odata)
    
    print >> jf, line

tf.close()

jf.close()

sf = open(sfile,"write")

sf.write(subcmd)

sf.close()

ok = call("qsub %s"%sfile,shell=True)
