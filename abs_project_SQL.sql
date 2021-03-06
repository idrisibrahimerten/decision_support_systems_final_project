USE [absuzmansistem]
GO
/****** Object:  Table [dbo].[cevaplar]    Script Date: 29/06/2022 16:19:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[cevaplar](
	[cid] [int] IDENTITY(1,1) NOT NULL,
	[cevap] [varchar](1) NULL,
	[sid] [int] NULL,
	[sonid] [int] NULL,
 CONSTRAINT [PK_cevaplar] PRIMARY KEY CLUSTERED 
(
	[cid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[islemsonuclari]    Script Date: 29/06/2022 16:19:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[islemsonuclari](
	[isid] [int] IDENTITY(1,1) NOT NULL,
	[hiz] [float] NULL,
	[frenbasinci] [float] NULL,
	[egim] [float] NULL,
 CONSTRAINT [PK_islemsonuclari] PRIMARY KEY CLUSTERED 
(
	[isid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sonuclar]    Script Date: 29/06/2022 16:19:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sonuclar](
	[sonid] [int] IDENTITY(1,1) NOT NULL,
	[sonuclarAd] [nvarchar](100) NULL,
 CONSTRAINT [PK_sonuclar_1] PRIMARY KEY CLUSTERED 
(
	[sonid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[sorular]    Script Date: 29/06/2022 16:19:25 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[sorular](
	[sid] [int] IDENTITY(1,1) NOT NULL,
	[sorular] [varchar](1000) NULL,
 CONSTRAINT [PK_sorular] PRIMARY KEY CLUSTERED 
(
	[sid] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [dbo].[cevaplar]  WITH CHECK ADD  CONSTRAINT [FK_cevaplar_sonuclar1] FOREIGN KEY([sonid])
REFERENCES [dbo].[sonuclar] ([sonid])
GO
ALTER TABLE [dbo].[cevaplar] CHECK CONSTRAINT [FK_cevaplar_sonuclar1]
GO
ALTER TABLE [dbo].[cevaplar]  WITH CHECK ADD  CONSTRAINT [FK_cevaplar_sorular] FOREIGN KEY([sid])
REFERENCES [dbo].[sorular] ([sid])
GO
ALTER TABLE [dbo].[cevaplar] CHECK CONSTRAINT [FK_cevaplar_sorular]
GO
