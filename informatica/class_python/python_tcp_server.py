#Milton Orlando Sarria Paja
#USC
#socket threading
import socket
import threading

class getSample(threading.Thread):
      ''' This creates a new thread to get samples or data
      '''
      #TO DO:
      def __init__(self, portnum=5000,buff_len=1024,name=None):
            threading.Thread.__init__(self)
            self.buff_len  = buff_len #how many bytes are you going to read? 4096 should be fine
            self.name      = name #to know if there is any other thread, you can name them differently
            self.port      = portnum                                              
            self.Continue  =  True            
      def run(self):            
            Continue = True
            socket_obj = socket.socket() 	
            host = socket.gethostname()  	
            socket_obj.bind((host, self.port)) 	
            socket_obj.listen(5)      		
            print 'Server started....'    
            # Establish connection with only ONE client.
            c, addr = socket_obj.accept() 
            print 'Connected by', addr
            while 1: 
                msgin = c.recv(self.buff_len)                                
                # Close the connection
                if not msgin: 
                    break
                if msgin == 'exit':                     
                    break
                else:
                    print msgin[1:50]
                    c.send('Done')
                    
            c.close()            
            socket_obj.close()
            del c
            del socket_obj
            print 'Leaving sampling thread....' 
            return
            
#######################################################
#                                                                                                                                     #
#                                        CALL MAIN FUNCTION                                                             #
#                                                                                                                                     #
#######################################################             
def main():
    serverThread = getSample(5006,4096,"Sampling-1")
    serverThread.start()


if __name__ == '__main__':
    main()
