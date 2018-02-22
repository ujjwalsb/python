#!/usr/bin/python

for a in range(0,5):
	for b in range(0,a+1):
		print "*",
	print

# *
# * *
# * * *
# * * * *
# * * * * *
print "==============================="

# ------------------------------------------------

for c in range(0,5):
	for d in range(0, 5-c):
		print "*",
	print

# * * * * *
# * * * *
# * * *
# * *
# *
print "==============================="

# --------------------------------------------------

for e in range(0,5):
	for f in range(0, 5-e):
		print "",
	for g in range(0, e+1):
		print "*",
	print

#     *
#    * *
#   * * *
#  * * * *
# * * * * *
print "==============================="

# --------------------------------------------------

for h in range(0,5):
	for i in range(0, h+1):
 		print "",
 	for j in range(0, 5-h):
 		print "*",
 	print

  # * * * * *
  # * * * *
  #  * * *
  #   * *
  #    *
print "==============================="

# --------------------------------------------------

for k in range(0,5):
	for l in range(0, 5-k):
		print "",
	for m in range(0, k+1):
		print "*",
	print
for k in range(0,5):
	for l in range(0, 1+k):
 		print "",
 	for m in range(0, 5-k):
 		print "*",
 	print

 #     *
 #    * *
 #   * * *
 #  * * * *
 # * * * * *
 # * * * * *
 #  * * * *
 #   * * *
 #    * *
 #     *