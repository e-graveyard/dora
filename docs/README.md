# D.O.R.A.

[![Build Status](https://travis-ci.com/caianrais/dora.svg?token=ENjnKFCm1zJx3evAtMkF&branch=master)](https://travis-ci.com/caianrais/dora)

**D**NS **O**ver **R**EST **A**PI.

**DORA** is a web application that provides a simple API for DNS querying through
a REST architecture. It aims to be a consumable API that's easy to digest and
easy to deploy in cloud-based solutions, such as Google App Engine.

**DORA** relies on `dnspython` toolkit and the `flask` microframework.


## Usage

```http
GET /dora/v1.0/mx/github.com
```

```js
{
  "code": 200,
  "data": {
    "answer": {
      "records": [
        {
          "hostname": "ALT3.ASPMX.L.GOOGLE.com.", 
          "priority": 10
        }, 
        {
          "hostname": "ALT1.ASPMX.L.GOOGLE.com.", 
          "priority": 5
        }, 
        {
          "hostname": "ALT4.ASPMX.L.GOOGLE.com.", 
          "priority": 10
        }, 
        {
          "hostname": "ALT2.ASPMX.L.GOOGLE.com.", 
          "priority": 5
        }, 
        {
          "hostname": "ASPMX.L.GOOGLE.com.", 
          "priority": 1
        }
      ]
    }, 
    "question": {
      "record": "MX", 
      "target": "github.com"
    }
  }, 
  "message": "DNS lookup is successful.", 
  "status": "success"
}
```

