import java.util.*;
import java.io.*;

public class Game
{
	private static ArrayList<Question> questions = new ArrayList<>();
	
	public static void main(String[] args) throws IOException
	{
		String[] options;
		String pattern = "[0-9]{1,}";
		ArrayList<Integer> alreadyUsed = new ArrayList<>();
		int correct = 0;
		int incorrect = 0;
		int temp;
		Question currentQuestion;
		Scanner in = new Scanner(System.in);
		String input;
		
		if(readFiles())
		{
			System.out.println("Welcome!");
			for(int i = 0; i < questions.size(); i++)
			{
				System.out.println("\n\nNext question:");
				input = "";
				currentQuestion = questions.get(i);
				System.out.println(currentQuestion.getQuestion());
				if(currentQuestion.getHasOptions())
				{
					alreadyUsed.clear();
					options = currentQuestion.getOptions(); // 0 = question, 1 = answer
					while(alreadyUsed.size() != (options.length - 1))
					{
						temp = (int) (Math.random() * (options.length - 1) + 1);
						if(!alreadyUsed.contains(temp))
						{
							alreadyUsed.add(temp);
							//System.out.print(alreadyUsed.size() + "." + options[temp] + "\t\t");
							System.out.printf("%d.%-20s\t", alreadyUsed.size(), options[temp]);
							if(alreadyUsed.size() % 2 == 0)
								System.out.println();
						}
					}
					if(alreadyUsed.size() % 2 != 0)
						System.out.println();
					input = in.nextLine();
					if(input.matches(pattern))
					{
						temp = Integer.parseInt(input);
						input = options[alreadyUsed.get(temp - 1)];
					}
				}
				else
				{
					input = in.nextLine();
				}
				if(input.equalsIgnoreCase(currentQuestion.getAnswer()))
				{
					System.out.println("Correct Answer!");
					correct++;
				}
				else
				{
					System.out.println("Incorrect Answer.");
					System.out.println("The correct answer is: " + currentQuestion.getAnswer());
					incorrect++;
				}
			}
			if(correct == correct + incorrect)
			{
				System.out.println("\n\nCongratulations! You answered all questions correctly.");
			}
			else
				System.out.println("\n\nYou got " + correct + "/" + (incorrect + correct) + " questions correct.");
		}
		else
			System.out.println("ERROR: No questions loaded.");
	}
	
	public static boolean readFiles() throws IOException
	{
		File aFile;
		Scanner inFile;
		Question temp;
		String[] lineElements;
		String customFile, input;
		Scanner in = new Scanner(System.in);
		
		System.out.println("Do you want to use questions from the \"QuestionsNoOptions.txt\" file?  Y/N");
		input = in.nextLine();
		if(input.equalsIgnoreCase("Y"))
		{
			aFile = new File("Questions/QuestionsNoOptions.txt");
			if(aFile.exists())
			{
				inFile = new Scanner(aFile);
				while(inFile.hasNext())
				{
					lineElements = inFile.nextLine().split("@");
					temp = new Question(lineElements[0], lineElements[1]);
					questions.add(temp);
				}
				inFile.close();
			}
			else
				System.out.println("\"QuestionsNoOptions.txt\" file couldn't be loaded.");
		}
		System.out.println("Do you want to use questions from the \"QuestionsOptions.txt\" file?  Y/N");
		input = in.nextLine();
		if(input.equalsIgnoreCase("Y"))
		{
			aFile = new File("Questions/QuestionsOptions.txt");
			if(aFile.exists())
			{
				inFile = new Scanner(aFile);
				while(inFile.hasNext())
				{
					lineElements = inFile.nextLine().split("@");
					temp = new Question(lineElements);
					questions.add(temp);
				}
				inFile.close();
			}
			else
				System.out.println("\"QuestionsOptions.txt\" file couldn't be loaded.");
		}
		if(questions.size() == 0)
			return false;
		return true;
	}
}