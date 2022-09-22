# Personal Website Overview
An open source project to build my personal website.

## Frontend
[personal-website-frontend-2020](https://github.com/IsaacOrzDev/personal-website-frontend-2020)

### Featuring

- Typescript
- React.js
- scss for styling
- redux for state management
- react-spring for animations

## API
I have implemented a simple API with AWS lambda function to get data from a json file that is stored in AWS S3.

```
'use strict';

const AWS = require('aws-sdk');
const S3 = new AWS.S3({ region: 'REGION' });

module.exports.data = async (event) => {
  const headers = {
    'Access-Control-Allow-Origin': 'https://isaacdev.com',
    'Access-Control-Allow-Credentials': true,
  };

  try {
    const data = await S3.getObject({
      Bucket: 'BUCKET',
      Key: 'data.json',
    }).promise();

    return {
      statusCode: 200,
      headers,
      body: JSON.stringify(JSON.parse(data.Body)),
    };
  } catch (err) {
    return {
      statusCode: err.statusCode || 500,
      headers,
      body: err.message || JSON.stringify(err.message),
    };
  }
};
```
