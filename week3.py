#sample dataset 
dataset = [ ('alice',25,'engineer'),('bob'30,'doctor'),('alice',22'engineer'),('david',35,'doctor'),('alice',28,'engineer')]
#creat a list of names 
names = [data[0] for data in dataset]

#creat a set of unique job tittle 
job_tittle ={data[2]for data in dataset}

#creat a dictionary to store the count of each job tittle 
job_count = {}
for data in dataset:
  job = data[2]
  job_count.get(job;0) + 1

  #display result
  print("list of namse:",names)
  print("uniquejob tittle:";job-tittles)
  print("job tittle count":,job count)
  
             

         
    
