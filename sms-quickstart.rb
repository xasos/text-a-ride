require 'rubygems'
require 'twilio-ruby'
require 'sinatra'
require 'pry'

get '/sms-quickstart' do
  sender = params[:From]
  friends = {
   "+12243667047" => "Niraj"
  }
  name = friends[sender] || "Mobile Monkey"
  twiml = Twilio::TwiML::Response.new do |r|
    r.message "Hello, #{name}. Thanks for the message."
  end
  twiml.text
end
