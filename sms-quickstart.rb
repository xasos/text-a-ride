require 'rubygems'
require 'twilio-ruby'
require 'sinatra'
require 'pry'

get '/sms-quickstart' do
  twiml = Twilio::TwiML::Response.new do |r|
    r.message "Message"
  end
  twiml.text
end
