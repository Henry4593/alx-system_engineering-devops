#!/usr/bin/env ruby
parsed_msg = /(?:(?<=from:)(?:\p{L}+|\+?\d+)|(?<=to:)(?:\p{L}+|\+?\d*)|(?<=flags:)(?:-?\d+:?)*)/
puts ARGV[0].scan(parsed_msg).join(',')
