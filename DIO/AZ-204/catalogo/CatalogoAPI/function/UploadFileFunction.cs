using System;
using System.IO;
using System.Threading.Tasks;
using Azure.Storage.Blobs;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Azure.WebJobs;
using Microsoft.Azure.WebJobs.Extensions.Http;
using Microsoft.AspNetCore.Http;
using Microsoft.Extensions.Logging;

namespace CatalogoAPI.Functions
{
    public static class UploadFileFunction
    {
        [FunctionName("UploadFile")]
        public static async Task<IActionResult> Run(
            [HttpTrigger(AuthorizationLevel.Function, "post", Route = null)] HttpRequest req,
            ILogger log)
        {
            string connectionString = Environment.GetEnvironmentVariable("AzureWebJobsStorage");
            var blobClient = new BlobServiceClient(connectionString);
            var containerClient = blobClient.GetBlobContainerClient("imagens");

            await containerClient.CreateIfNotExistsAsync();

            string fileName = Guid.NewGuid().ToString() + ".jpg";
            var blob = containerClient.GetBlobClient(fileName);

            using (var stream = req.Body)
            {
                await blob.UploadAsync(stream);
            }

            return new OkObjectResult($"Arquivo salvo: {fileName}");
        }
    }
}
