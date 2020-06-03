package a2;
import java.util.Scanner;
public class PlayfairCipher
{
		private String KeyWord=new String();
		private String Key=new String();
		private char matrix_arr[][]= new char[5][5];
		public static void main(String[] args) 
		{
			Scanner s = new Scanner(System.in);
		    PlayfairCipher ob=new PlayfairCipher();
		    System.out.println("Enter the keyword:");
		    String keyword = s.nextLine();
		    ob.setKey(keyword);
		    ob.KeyGen();
		    System.out.println("Enter the text to encrypt and decrypt(withoutanyspaces):");
		    String key_input = s.next();
		    String Encrypted= ob.Encrypt(key_input);
		    ob.Decrypt(Encrypted);
		    s.close();
		}
		//This function will take the input key from the user
		//Then it'll remove duplication of letters from the key
		//Will add it to the private KeyWord for matrix generation
		public void setKey(String k)
		{
			String new_k=new String();
			boolean flag = false;
			new_k+= k.charAt(0);
			for(int i=1; i<k.length();i++)
			{
				for(int j=0;j<new_k.length(); j++)
				{ 
					if(k.charAt(i)==new_k.charAt(j))
					{
						flag = true;
					}
				}
				if(flag == false)
					new_k += k.charAt(i);
				flag = false;
			}
			KeyWord=new_k;
		}
		// This function adjust the alphabetical letters adding the
		// KeyWord on the beginning of them & then it calls the matrix function
		public void KeyGen()
		{
			boolean flag=true;
			Key=KeyWord;
			for ( int i=0 ; i<26 ; i++)
			{
				char current=(char)(i+97);
				if(current=='j')
					continue;
				for(int j=0 ; j< KeyWord.length() ; j++ )
				{
					if (current == KeyWord.charAt(j))
					{
						flag=false;
						break;
					}
				}

				if(flag)
					Key=Key+current;
				flag=true;
			}
			System.out.println("The sequence:"+Key);
			matrix ();
		}
		//The sequence is displayed as the matrix.
		private void matrix ()
		{
			int count=0;
			for (int i=0 ; i<5 ;i++)
			{
				for (int j=0 ; j<5 ; j++)
				{
					matrix_arr[i][j]=Key.charAt(count);
					System.out.printf("%s ",matrix_arr[i][j]);
					count++;
				}
				System.out.println();
			}
		}
		// This function is to adjust the Text to encrypt
		// It changes all the 'j' letters to 'i' & add 'x' character between repeatable pairs.
		private String format(String old_text)
		{
			int i = 0,len = 0;
			String text = new String();
			len = old_text.length();
			//System.out.println(old_text);
			// Change all j's into i's 
			for (int tmp = 0; tmp < len; tmp++)
			{
				if (old_text.charAt(tmp) == 'j')
				{
					text = text + 'i';
				}
				else
					text = text+old_text.charAt(tmp);
			}
			len = text.length();
			// Assign 'x' to letters that repeat in text.
			for (i = 0; i < len; i = i + 2) 
			{ 
				if (text.charAt(i+1) == text.charAt(i)) //if char = previous char
				{
					text = text.substring(0, i+1) + 'x' + text.substring(i+1);
				}
				else //not a repeat character, move along
				{}
			}
			return text;
		}
		private String [] Divid2Pairs (String new_string)
		{
			String Original = format(new_string);
			int size= Original.length();
			if(size%2!=0)
			{
				size++;
				Original = Original+'x';
			}
			String x[]= new String[size/2];
			int count=0;
			for ( int i=0 ; i<size/2 ;i++)
			{
				x[i]=Original.substring(count, count+2);
				System.out.println(x[i]);
				count=count+2;
			}
			return x;
		}
		
		public int[] GetDiminsions(char letter)
		{
			int []key=new int[2];
			if ( letter == 'j')
				letter='i';
			for (int i=0 ; i<5 ;i++)
			{
				for (int j=0 ; j<5 ; j++)
				{
					if(matrix_arr[i][j] == letter)
					{
						key[0]=i;
						key[1]=j;
						break;
					}
				}
			}
			return key;
		}

		public String Encrypt(String Source)
		{ 
			System.out.println("\n----------Encryption----------");
			String src_arr[]=Divid2Pairs(Source);
			String Code=new String();
			int part1[]=new int[2];
			int part2[]=new int[2];
			for (int i=0 ; i< src_arr.length ;i++ )//start on pair by pair
			{
				char one = src_arr[i].charAt(0);//get first char
				char two = src_arr[i].charAt(1);//get second char
				part1 = GetDiminsions(one);//get position of the first char
				part2 = GetDiminsions(two);//get position of the second char
				//check for special cases
				if(part1[0]==part2[0])//same row
				{
					if (part1[1]<4)
						part1[1]++;
					else
						part1[1]=0;
					if(part2[1]<4)
						part2[1]++;
					else
						part2[1]=0;
				}
				else if (part1[1]==part2[1]) //same column
				{
					if (part1[0]<4)
						part1[0]++;
					else
						part1[0]=0;
					if(part2[0]<4)
						part2[0]++;
					else
						part2[0]=0;
				}
				else
				{
					int temp=part1[1];
					part1[1]=part2[1];
					part2[1]=temp;
				}

				Code= Code + matrix_arr[part1[0]][part1[1]] + matrix_arr[part2[0]][part2[1]];
			}
			System.out.println(Code);
			return Code;
		}

		public String Decrypt (String Code)
		{
			System.out.println("\n----------Decryption----------");
			String Original=new String();
			String src_arr[]=Divid2Pairs(Code);
			int part1[]=new int[2];
			int part2[]=new int[2];
			for (int i=0 ; i< src_arr.length ;i++ )//start on pair by pair
			{
				char one = src_arr[i].charAt(0);//get first char
				char two = src_arr[i].charAt(1);//get second char
				part1 = GetDiminsions(one);//get position of the first char
				part2 = GetDiminsions(two);//get position of the second char
				//check for special cases
				if(part1[0]==part2[0])//same row
				{
					if (part1[1]>0)
						part1[1]--;
					else
						part1[1]=4;
					if(part2[1]>0)
						part2[1]--;
					else
						part2[1]=4;
				}
				else if (part1[1]==part2[1]) //same column
				{
					if (part1[0]>0)
						part1[0]--;
					else
						part1[0]=4;
					if(part2[0]>0)
						part2[0]--;
					else
						part2[0]=4;
				}
				else
				{
					int temp=part1[1];
					part1[1]=part2[1];
					part2[1]=temp;
				}

				Original =Original + matrix_arr[part1[0]][part1[1]] + matrix_arr[part2[0]][part2[1]];
			}
			System.out.println(Original);
			return Original;
		}
}