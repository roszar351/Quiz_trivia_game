public class Question
{
	private String theQuestion;
	private String answer;
	private String[] options; 
	private boolean hasOptions;
	
	public Question(String q, String a)
	{
		theQuestion = q;
		answer = a;
		hasOptions = false;
	}
	
	public Question(String[] o)
	{
		options = o;
		theQuestion = o[0];
		answer = o[1];
		hasOptions = true;
	}
	
	public String getQuestion()
	{
		return theQuestion;
	}
	
	public String getAnswer()
	{
		return answer;
	}
	
	public String[] getOptions()
	{
		return options;
	}
	
	public boolean getHasOptions()
	{
		return hasOptions;
	}
}