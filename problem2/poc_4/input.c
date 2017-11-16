#include <stdio.h>
#include <curl/curl.h>
 
int main(void)
{
  char *url = "%FF";  
  char *result = curl_easy_unescape(NULL, url, 1, NULL);
  printf("%s", result);
  return 0;
}
