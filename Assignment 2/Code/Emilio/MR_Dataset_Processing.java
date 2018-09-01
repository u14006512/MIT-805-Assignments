import java.io.IOException;

import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.Mapper;
import org.apache.hadoop.mapreduce.Reducer;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;
//import org.apache.hadoop.io.LongWritable;

public class MR_Dataset_Processing {
  public static class CrimesPerYearMapper
       extends Mapper<Object, Text, Text, IntWritable>{

    private final static IntWritable one = new IntWritable(1);
    private Text word = new Text();

    public void map(Object key, Text value, Context context
                    ) throws IOException, InterruptedException {
      
      String[] split = value.toString().split(","); // Split CSV lines by comma.
      
      word.set(split[9]);
      context.write(word, one);
	 
	  
	  
	  }
 }
 
  public static class GeneralReducer
       extends Reducer<Text,IntWritable,Text,IntWritable> {
    private IntWritable result = new IntWritable();

    public void reduce(Text key, Iterable<IntWritable> values,
                       Context context
                       ) throws IOException, InterruptedException {
      int sum = 0;
      for (IntWritable val : values) {
        sum += val.get();
      }
      result.set(sum);
      context.write(key, result);
    }
  }

public static class CrimesPerDistrictMapper
  extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
               ) throws IOException, InterruptedException {
 
 String[] split = value.toString().split(","); // Split CSV lines by comma.
 
 word.set("District:"+split[6]);
 context.write(word, one);

 
 
 }
}

public static class CrimesPerDistrictPerYearMapper
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

word.set(split[9]+"_"+split[6]);
context.write(word, one);

}
}

public static class CrimesPerTypeMapper
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

word.set(split[1]);
context.write(word, one);

}
}

public static class CrimesPerYearPerDistrictPerTypeMapper
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

word.set(split[9]+"_"+split[6]+"_"+split[1]);
context.write(word, one);

}
}

public static class ArrestsMapper
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

if (split[4].equals("true"))
{
	word.set("Arrest Successful");
	context.write(word, one);
} else 
	{
	word.set("Arrest Unsuccessful");
	context.write(word, one);
	}


}
}

public static class ArrestsPerYearMapper
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

if (split[4].equals("true"))
{
	word.set("Arrests_"+split[9]);
	context.write(word, one);
} else 
	{
	word.set("FailedArrests_"+split[9]);
	context.write(word, one);
	}
}
}

public static class CrimesPerWardMapper
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

	word.set("Ward:"+split[7]);
	context.write(word, one);

}
}

public static class CrimesPerBeatMapper
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

	word.set("Beat:"+split[8]);
	context.write(word, one);

}
}

public static class DomesticCrimesMapper
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

if (split[5].equals("true"))
{
	word.set("Domestic");
	context.write(word, one);
} else 
	{
	word.set("Not_Domestic");
	context.write(word, one);
	}

}
}

public static class DomesticCrimesResolutionMapper
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

if (split[5].equals("true"))
{
	if (split[4].equals("true"))
	{
		word.set("Domestic_Arrests");
		context.write(word, one);
	} else 
		{
		word.set("Domestic_Failed_Arrests");
		context.write(word, one);
		}
	
} 
}
}

public static class CrimesPerLocation
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

	if (split[3].equals(""))
	{
		word.set("Unknown_Location");
	} else {word.set(split[3]);}
	
	context.write(word, one);

}
}

public static class CrimesPerLocationPerTypeMapper
extends Mapper<Object, Text, Text, IntWritable>{

private final static IntWritable one = new IntWritable(1);
private Text word = new Text();

public void map(Object key, Text value, Context context
             ) throws IOException, InterruptedException {

String[] split = value.toString().split(","); // Split CSV lines by comma.

	if (split[3].equals(""))
	{
		word.set("Unknown_Location"+"_"+split[1]);
	} else {word.set(split[3]+"_"+split[1]);}

	context.write(word, one);

}
}

public static void main(String[] args) throws Exception {
	Path out = new Path(args[1]);  
	Configuration conf = new Configuration();
    
    Job job = Job.getInstance(conf, "Basic Reduce Job 1: Crimes per Year");
    job.setJarByClass(MR_Dataset_Processing.class);
    job.setMapperClass(CrimesPerYearMapper.class);
    job.setCombinerClass(GeneralReducer.class);
    job.setReducerClass(GeneralReducer.class);
    job.setOutputKeyClass(Text.class);
    job.setOutputValueClass(IntWritable.class);
    
    job.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job, new Path(args[0]));
    FileOutputFormat.setOutputPath(job, new Path(out, "Crimes_Per_Year"));
    if (!job.waitForCompletion(true)) {
    	  System.exit(1);
    }
    
    System.out.println("Crimes Per Year Completed");
     
    Job job2 = Job.getInstance(conf, "Basic Reduce Job 2: Crimes per District");
    job2.setJarByClass(MR_Dataset_Processing.class);
    job2.setMapperClass(CrimesPerDistrictMapper.class);
    job2.setCombinerClass(GeneralReducer.class);
    job2.setReducerClass(GeneralReducer.class);
    job2.setOutputKeyClass(Text.class);
    job2.setOutputValueClass(IntWritable.class);
    
    job2.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job2, new Path(args[0]));
    FileOutputFormat.setOutputPath(job2, new Path(out, "Crimes_Per_District"));
    if (!job2.waitForCompletion(true)) {
    	  System.exit(1);
    }
    System.out.println("Crimes Per District Completed");
    
    Job job3 = Job.getInstance(conf, "Basic Reduce Job 3: Crimes per Year Per District");
    job3.setJarByClass(MR_Dataset_Processing.class);
    job3.setMapperClass(CrimesPerDistrictPerYearMapper.class);
    job3.setCombinerClass(GeneralReducer.class);
    job3.setReducerClass(GeneralReducer.class);
    job3.setOutputKeyClass(Text.class);
    job3.setOutputValueClass(IntWritable.class);
    
    job3.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job3, new Path(args[0]));
    FileOutputFormat.setOutputPath(job3, new Path(out, "Crimes_Per_Year_Per_District"));
    if (!job3.waitForCompletion(true)) {
    	  System.exit(1);
    }
    System.out.println("Crimes Per Type");
    
    Job job4 = Job.getInstance(conf, "Basic Reduce Job 4: Crimes per Type");
    job4.setJarByClass(MR_Dataset_Processing.class);
    job4.setMapperClass(CrimesPerTypeMapper.class);
    job4.setCombinerClass(GeneralReducer.class);
    job4.setReducerClass(GeneralReducer.class);
    job4.setOutputKeyClass(Text.class);
    job4.setOutputValueClass(IntWritable.class);
    
    job4.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job4, new Path(args[0]));
    FileOutputFormat.setOutputPath(job4, new Path(out, "Crimes_Per_Type"));
    if (!job4.waitForCompletion(true)) {
    	  System.exit(1);
    }
    System.out.println("Crimes Per Type Completed");
    
    
    Job job5 = Job.getInstance(conf, "Basic Reduce Job 5: Crimes Per Year Per District Per Type ");
    job5.setJarByClass(MR_Dataset_Processing.class);
    job5.setMapperClass(CrimesPerYearPerDistrictPerTypeMapper.class);
    job5.setCombinerClass(GeneralReducer.class);
    job5.setReducerClass(GeneralReducer.class);
    job5.setOutputKeyClass(Text.class);
    job5.setOutputValueClass(IntWritable.class);
    
    job5.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job5, new Path(args[0]));
    FileOutputFormat.setOutputPath(job5, new Path(out, "Crimes_Per_Year_Per_District_Per_Type"));
    if (!job5.waitForCompletion(true)) {
    	  System.exit(1);
    }
    
    Job job6 = Job.getInstance(conf, "Basic Reduce Job 6: Arrests");
    job6.setJarByClass(MR_Dataset_Processing.class);
    job6.setMapperClass(ArrestsMapper.class);
    job6.setCombinerClass(GeneralReducer.class);
    job6.setReducerClass(GeneralReducer.class);
    job6.setOutputKeyClass(Text.class);
    job6.setOutputValueClass(IntWritable.class);
    
    job6.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job6, new Path(args[0]));
    FileOutputFormat.setOutputPath(job6, new Path(out, "Number_of_Arrests"));
    if (!job6.waitForCompletion(true)) {
    	  System.exit(1);
    }
    
    Job job7 = Job.getInstance(conf, "Basic Reduce Job 6: Arrests Per Year");
    job7.setJarByClass(MR_Dataset_Processing.class);
    job7.setMapperClass(ArrestsPerYearMapper.class);
    job7.setCombinerClass(GeneralReducer.class);
    job7.setReducerClass(GeneralReducer.class);
    job7.setOutputKeyClass(Text.class);
    job7.setOutputValueClass(IntWritable.class);
    
    job7.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job7, new Path(args[0]));
    FileOutputFormat.setOutputPath(job7, new Path(out, "Number_of_Arrests_Per_Year"));
    if (!job7.waitForCompletion(true)) {
    	  System.exit(1);
    }

    Job job8 = Job.getInstance(conf, "Basic Reduce Job 7: Crimes Per Ward");
    job8.setJarByClass(MR_Dataset_Processing.class);
    job8.setMapperClass(CrimesPerWardMapper.class);
    job8.setCombinerClass(GeneralReducer.class);
    job8.setReducerClass(GeneralReducer.class);
    job8.setOutputKeyClass(Text.class);
    job8.setOutputValueClass(IntWritable.class);
    
    job8.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job8, new Path(args[0]));
    FileOutputFormat.setOutputPath(job8, new Path(out, "Crimes_Per_Ward"));
    if (!job8.waitForCompletion(true)) {
    	  System.exit(1);
    }
    
    Job job9 = Job.getInstance(conf, "Basic Reduce Job 8: Crimes Per Beat");
    job9.setJarByClass(MR_Dataset_Processing.class);
    job9.setMapperClass(CrimesPerBeatMapper.class);
    job9.setCombinerClass(GeneralReducer.class);
    job9.setReducerClass(GeneralReducer.class);
    job9.setOutputKeyClass(Text.class);
    job9.setOutputValueClass(IntWritable.class);
    
    job9.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job9, new Path(args[0]));
    FileOutputFormat.setOutputPath(job9, new Path(out, "Crimes_Per_Beat"));
    if (!job9.waitForCompletion(true)) {
    	  System.exit(1);
    }
    
    Job job10 = Job.getInstance(conf, "Basic Reduce Job 9: Domestic Crimes");
    job10.setJarByClass(MR_Dataset_Processing.class);
    job10.setMapperClass(DomesticCrimesMapper.class);
    job10.setCombinerClass(GeneralReducer.class);
    job10.setReducerClass(GeneralReducer.class);
    job10.setOutputKeyClass(Text.class);
    job10.setOutputValueClass(IntWritable.class);
    
    job10.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job10, new Path(args[0]));
    FileOutputFormat.setOutputPath(job10, new Path(out, "Domestic_Crimes"));
    if (!job10.waitForCompletion(true)) {
    	  System.exit(1);
    }
    
    Job job11 = Job.getInstance(conf, "Basic Reduce Job 10: Domestic Crimes Arrests");
    job11.setJarByClass(MR_Dataset_Processing.class);
    job11.setMapperClass(DomesticCrimesResolutionMapper.class);
    job11.setCombinerClass(GeneralReducer.class);
    job11.setReducerClass(GeneralReducer.class);
    job11.setOutputKeyClass(Text.class);
    job11.setOutputValueClass(IntWritable.class);
    
    job11.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job11, new Path(args[0]));
    FileOutputFormat.setOutputPath(job11, new Path(out, "Domestic_Crimes_Resolution"));
    if (!job11.waitForCompletion(true)) {
    	  System.exit(1);
    }
    
    Job job12 = Job.getInstance(conf, "Basic Reduce Job 11: Crimes Per Location");
    job12.setJarByClass(MR_Dataset_Processing.class);
    job12.setMapperClass(CrimesPerLocation.class);
    job12.setCombinerClass(GeneralReducer.class);
    job12.setReducerClass(GeneralReducer.class);
    job12.setOutputKeyClass(Text.class);
    job12.setOutputValueClass(IntWritable.class);
    
    job12.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job12, new Path(args[0]));
    FileOutputFormat.setOutputPath(job12, new Path(out, "Crimes_Per_Location"));
    if (!job12.waitForCompletion(true)) {
    	  System.exit(1);
    }
    
    Job job13 = Job.getInstance(conf, "Basic Reduce Job 12: Crimes Per Location Per Type");
    job13.setJarByClass(MR_Dataset_Processing.class);
    job13.setMapperClass(CrimesPerLocationPerTypeMapper.class);
    job13.setCombinerClass(GeneralReducer.class);
    job13.setReducerClass(GeneralReducer.class);
    job13.setOutputKeyClass(Text.class);
    job13.setOutputValueClass(IntWritable.class);
    
    job13.setOutputFormatClass(org.apache.hadoop.mapreduce.lib.output.TextOutputFormat.class);
    FileInputFormat.addInputPath(job13, new Path(args[0]));
    FileOutputFormat.setOutputPath(job13, new Path(out, "Crimes_Per_Location_Per_Type"));
    if (!job13.waitForCompletion(true)) {
    	  System.exit(1);
    }
    
    System.out.println("HADOOP JOBS FINISHED!");
    System.out.println("HAVE A NICE DAY!");
  	}
	
}


