package test;
import java.net.*;
import java.io.*;
import java.util.Scanner;
public class Client {
  public static void main(String args[]) throws IOException {
	Scanner sc=new Scanner(System.in); 
	//Server application makes a ServerSocket on a specific port.
	//Server listening for client requests coming in for port no as which server is choosen.
    System.out.println("\nEnter the port no where sever is ready to listen:");
    //server is running on port no:1001
    int port=Integer.parseInt(sc.nextLine()); 
    // 127.0.0.1  is the IP address of local host, where code will run on single stand-alone machine
    Socket s1 = new Socket("127.0.0.1",port);
	InputStream is = s1.getInputStream();
    DataInputStream dis = new DataInputStream(is);
    String str = new String (dis.readUTF());
    //readUTF():method of DataInputStream class reads from the stream in a representation
  	//of a Unicode character string encoded in modified UTF-8 format. 
  	//This string of characters is then returned as a String.
    System.out.println(str);
	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    System.out.print("Enter data to send : ");
	OutputStream os = s1.getOutputStream();
    PrintWriter pwrite = new PrintWriter(os, true);
    //PrintWriter:The primitive data  is formatted as text, rather than as their byte values.
	String message= br.readLine(); // Reading the data from the IO 
    pwrite.println(message);       // sending to server
    s1.close();
    sc.close();
  }
}

