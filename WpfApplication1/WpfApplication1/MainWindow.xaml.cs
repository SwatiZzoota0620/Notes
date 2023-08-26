using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Windows.Media.Animation;

namespace WpfApplication1
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }
        

        private void image1_MouseLeave_1(object sender, MouseEventArgs e)
        {
            Image img = (Image)sender;
            DoubleAnimation am = new DoubleAnimation(0, TimeSpan.FromSeconds(2));
            img.BeginAnimation(Image.OpacityProperty, am);

        }

        private void image1_MouseEnter_1(object sender, MouseEventArgs e)
        {
            Image img = (Image)sender;
            DoubleAnimation am = new DoubleAnimation(1, TimeSpan.FromSeconds(3));
            img.BeginAnimation(Image.OpacityProperty, am);

        }

       

       
    }
}
