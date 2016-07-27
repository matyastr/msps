using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Drawing;
using Microsoft.Win32;
using System.Xml;
using System.Net.Http;
using System.Net.Http.Headers;
using Newtonsoft.Json.Linq;
using System.Net;

namespace MSPSClient
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        private const string SERVICE_URI = "http://localhost:55360";
        private const string RESOURCE = "compare";

        public MainWindow()
        {
            InitializeComponent();
        }

        private void BtnBrowse_Click(object sender, RoutedEventArgs e)
        {
            Cursor = Cursors.Wait;

            var fileDialog = new OpenFileDialog()
            {
                Filter = "XML Files|*.xml",
                Title = "Select a MusicXML File"
            };

            var result = fileDialog.ShowDialog();

            if (result.HasValue && (bool)result) 
            {
                txtBrowse.Text = fileDialog.FileName;
            }

            Cursor = null;
        }

        private void BtnCompare_Click(object sender, RoutedEventArgs e)
        {
            if (string.IsNullOrEmpty(txtBrowse.Text))
            {
                MessageBox.Show("Please select a file.", "No File Selected", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            if (!File.Exists(txtBrowse.Text))
            {
                MessageBox.Show("Please select another file.", "File Does Not Exist", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            dtgResults.ItemsSource = null;

            Compare();
        }

        private void Compare()
        {
            Cursor = Cursors.Wait;

            var musicXmlDoc = new XmlDocument();

            try
            {
                musicXmlDoc.Load(txtBrowse.Text);
            }
            catch (XmlException ex)
            {
                MessageBox.Show("Please fix the selected document or select another.", "Invalid XML Document", MessageBoxButton.OK, MessageBoxImage.Error);
                return;
            }

            var response = RetrieveResultsFromService(musicXmlDoc);

            if (!string.IsNullOrEmpty(response))
            {
                var jsonResponse= JObject.Parse(response);
                var resultsSet = jsonResponse.SelectToken("$.results");

                var itemsSourceList = new List<ResultRow>();

                foreach (JProperty prop in resultsSet)
                {
                    var newRow = new ResultRow()
                    {
                        Title = prop.Name.Split('|')[0],
                        Composer = prop.Name.Split('|')[1],
                        Similarity = prop.Value.ToString()
                    };

                    itemsSourceList.Add(newRow);
                }

                dtgResults.ItemsSource = itemsSourceList;
            }

            Cursor = null;
        }

        private string RetrieveResultsFromService(XmlDocument musicXmlDoc)
        {
            var httpWebRequest = (HttpWebRequest)WebRequest.Create(SERVICE_URI + "/" + RESOURCE);
            httpWebRequest.Method = "POST";

            using (var streamWriter = new StreamWriter(httpWebRequest.GetRequestStream()))
            {
                streamWriter.Write(musicXmlDoc.OuterXml);
                streamWriter.Flush();
            }

            var httpResponse = (HttpWebResponse)httpWebRequest.GetResponse();

            string result = string.Empty;

            using (var streamReader = new StreamReader(httpResponse.GetResponseStream()))
            {
                result = streamReader.ReadToEnd();
            }

            return result;
        }

        public class ResultRow
        {
            public string Title { get; set; }
            public string Composer { get; set; }
            public string Similarity { get; set; }
        }
    }
}
