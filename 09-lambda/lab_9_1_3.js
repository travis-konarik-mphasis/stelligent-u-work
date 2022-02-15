exports.handler = async (event) => {
            const body = JSON.parse(event.body)
            const value = body.value ? body.value : "AWS";
            const response = {
              statusCode: 200,
              body: JSON.stringify('Hello ' + value + '!'),
            };
          return response;
          };