/*
Windows 8.1, Visual Studio 2017
Simple SHA1 bruteforce work with dictionary file
by @rextco

To make a dictionary use crunch on Linux
crunch 8 8 -t %%%%%%%% -o 8-numbers.txt

To OpenSSL use this: https://www.npcglib.org/~stathis/downloads/openssl-1.1.0f-vs2017.7z
To configure OpenSSL: https://stackoverflow.com/questions/32156336/how-to-include-openssl-in-visual-studio-expres-2012-windows-7-x64
*/

#include <openssl/sha.h>
#include <stdio.h>
#include <fstream>
#include <string>	// getline

#pragma comment(lib, "libcryptoMT.lib")

// https://stackoverflow.com/questions/11236216/coverting-unsigned-char-returned-from-sha1-to-a-string
char* hash_to_string(unsigned char* bytes) {
	char hash_string[SHA_DIGEST_LENGTH * 2 + 1];
	for (int i = 0; i < SHA_DIGEST_LENGTH; i++) {
		snprintf(hash_string + i * 2, 3, "%02x ", bytes[i]);
	}	
	return hash_string;
}


int main(int argc, const char* argv[]) {	
	const char TARGET_HASH[] = "8e2b0f24e6f22012b834bde961cc4cc1bb6c6880";			// SHA1 to broke
	
	unsigned char digest[SHA_DIGEST_LENGTH] = {};
	char* hash_string;
	
	std::string input_filename = "D:\\share\\8-numbers.txt";
	std::string word_of_file;
	
	std::ifstream input_data_stream;
	input_data_stream.open(input_filename.c_str(), std::ios_base::in | std::ios_base::binary);
	unsigned int attempts = 0;
	while (std::getline(input_data_stream, word_of_file)) {
		if (!word_of_file.empty()) {
			// SHA1 return a sequence of bytes
			SHA1((const unsigned char*)word_of_file.c_str(), word_of_file.size(), digest);	// SHA1 of word_bytes
			hash_string = hash_to_string(digest);
			
			// SHA1((unsigned char*)hash_string, strlen(hash_string), digest);					//# SHA1 again of prev SHA1
			// hash_string = hash_to_string(digest);

			if( strcmp(hash_string, TARGET_HASH) == 0 ) {
				printf_s("\n==> Founded: word = %s | hash = %s | attempts = %d", word_of_file.c_str(), hash_string, attempts);
				break;
			}
			
			if (attempts % (1 << 20) == 0) {
				printf_s("debug!control: word = %s | hash = %s | attempts = %d\n", word_of_file.c_str(), hash_string, attempts);
			}
			attempts++;
		}
	}

	input_data_stream.close();		
	return 0;
}