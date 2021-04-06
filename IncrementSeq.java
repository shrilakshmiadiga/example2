package practice;

public class IncrementSeq extends Thread
{
	
	 static Object ob = new Object();
	 static int cnt = 0;
	
	 public void run () 
	 {
		 Increment();
	 }
		void Increment(){
		synchronized(ob){
		try 
		{
		   String tName =  Thread.currentThread().getName();
		  
		   int tNum = Integer.parseInt(tName.substring(7,tName.length())); 
		   
		   	while(tNum != cnt)
		   		{
		   			ob.wait();
		   		}
		  
		   cnt++;
		   System.out.println(tName+" is running. Counter value :"+cnt); 
		  
		   ob.notifyAll();
	   }
	 
	   catch (Exception e) 
	   {
		   System.out.println(e.getMessage());
	   }
	  
	  }
		
	 }
	 
 
	 public static void main(String[] args) 
	 {
	
		  try {
			  for(int i = 0; i < 50; i++)
			  	{
				  IncrementSeq t = new IncrementSeq();
				  t.start();
			  	}	
		  	}
		  catch(Exception e)
		  {
			  System.out.println(e.getMessage());
		  }
	 }
}
