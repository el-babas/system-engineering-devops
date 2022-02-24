#!/usr/bin/env ruby
# The regular expression must match a 10 digit phone number
puts ARGV[0].scan(/^[0-9]{10}$/).join
