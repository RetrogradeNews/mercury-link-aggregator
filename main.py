import os
import pandas as pd

from scraping import scrapeLinks

def main():
  csvLocation = os.path.join('data', 'rg.csv')
  dataLocation = os.path.join("data", "mercury_links.csv")

  # Loads csv without "views" column
  df = pd.read_csv(csvLocation, names=["title", "views", "url"]).drop('views', axis=1)
  
  print("Beginning scrape!")

  # Scrapes the url for any hyperlinks that lead to the The Mercury
  df['merc_links'] = df['url'].apply(scrapeLinks)

  # Drops all pieces without references to The Mercury
  df = df.dropna()

  # Makes an entry for every individual The Mercury hyperlink
  df = df.explode('merc_links')

  # Saves data to csv
  df.to_csv(dataLocation, index=False)
  
  print("Done!")
        

# Swag-based print statements
def swag():
    print("""                             ..                                
                    ...                 .                      
                .                            .                 
             .                                  .              
           .                                       .           
         .                                          ..         
                                                      .        
      .                                                        
                    #%%%%%%%%##%%%#-                     .     
   .                   .%%%       -%%%.                   .    
                        %%%        :%%%+++++++++-.         .   
                        %%%    ..++=%%%.       :+++.           
                        %%% .++.    %%%           ++           
                        %%%.       .%%.            +.          
                      .+%%%        %*              =           
                    =:  %%%*==+*%%.               .:          .
                  =.    %%%    .%%%.             .:            
                =       %%%      #%%+           .:            .
              .:        %%%       -%%%.        =               
             -          %%%        .%%%:     :.               .
            +           %%%          *%%%. :.                  
           +=           %%%           .%%*#                  . 
 .         +-          .%%%           .-=%%%%.                 
  .       :++       **+=====+*+    -=.    -******              
           +++.               .=+.                             
            +++++=--:--=+++++.                            .    
     .        .-=++++=-:                                       
      .                                                        
                                                      .        
                                                               
           .                                                   
              .                                 .              
                 .                                             
                      .                 .                      
    """)
    print("\"THE RETROGRADE\"")
    print("LINK AGGREGATOR BY MUAAZ ABED\n")

if __name__ == "__main__":
  swag()
  main()