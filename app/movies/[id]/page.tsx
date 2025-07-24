// frontend/app/movies/[id]/page.tsx
'use client';

import { useState, useEffect } from 'react';
import { useParams, useRouter } from 'next/navigation';
import Link from 'next/link';
import Image from 'next/image';
import {
  Container, Typography, Box, Paper, Button, Rating, Alert, CircularProgress, Divider, Chip,
  Dialog, DialogActions, DialogContent, DialogContentText, DialogTitle
} from '@mui/material';

// 映画データの型定義
interface Movie {
  id: number;
  title: string;
  genres: string;
  director: string;
  actors: string;
  release_year: number | null;
  country: string;
  movie_poster: string | null;
  rating: number | null;
  impressions: string;
  watch_method: string;
  watched_date: string | null;
}

export default function MovieDetailPage() {
  const params = useParams();
  const router = useRouter();
  const id = params.id as string;

  const [movie, setMovie] = useState<Movie | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [openDeleteDialog, setOpenDeleteDialog] = useState(false); // 削除確認ダイアログの状態

  useEffect(() => {
    if (!id) return;

    const fetchMovie = async () => {
      setIsLoading(true);
      setError(null);
      try {
        const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';
        const response = await fetch(`${backendUrl}/api/movies/${id}/`);

        if (!response.ok) {
          throw new Error('映画データの読み込みに失敗しました。');
        }
        const data = await response.json();
        setMovie(data);
      } catch (err: any) {
        setError(err.message);
      } finally {
        setIsLoading(false);
      }
    };

    fetchMovie();
  }, [id]);

  // 画像URLを安全に解決する関数
  const getImageUrl = (path: string | null) => {
    if (!path) return '/placeholder_movie.jpg';
    if (path.startsWith('http')) return path;
    return `http://localhost:8000/media/${path}`;
  };

  // --- 削除機能の追加 ---
  const handleDeleteDialogOpen = () => setOpenDeleteDialog(true);
  const handleDeleteDialogClose = () => setOpenDeleteDialog(false);

  const handleDelete = async () => {
    handleDeleteDialogClose();
    setIsLoading(true);
    setError(null);
    try {
      const backendUrl = process.env.NEXT_PUBLIC_BACKEND_URL || 'http://localhost:8000';
      const response = await fetch(`${backendUrl}/api/movies/${id}/`, {
        method: 'DELETE',
      });

      if (!response.ok) {
        throw new Error('映画の削除に失敗しました。');
      }

      alert('映画の記録を削除しました。');
      router.push('/movies/list'); // 削除後に一覧ページへ移動
    } catch (err: any) {
      setError(err.message);
      setIsLoading(false);
    }
  };
  // --- ここまで削除機能 ---

  if (isLoading && !movie) { // 初回ロード時
    return <Container sx={{ py: 4, textAlign: 'center' }}><CircularProgress /></Container>;
  }

  if (error || !movie) {
    return (
      <Container sx={{ py: 4, textAlign: 'center' }}>
        <Alert severity="error">{error || '映画が見つかりません。'}</Alert>
        <Button component={Link} href="/movies/list" sx={{ mt: 2 }}>一覧に戻る</Button>
      </Container>
    );
  }

  return (
    <>
      <Container maxWidth="md" sx={{ py: 5 }}>
        <Paper elevation={3} sx={{ p: { xs: 2, sm: 4 } }}>
          {/* ... (映画の詳細表示部分は変更なし) ... */}
          <Box sx={{ display: 'flex', flexDirection: { xs: 'column', sm: 'row' }, gap: 4 }}>
            <Box sx={{ width: { xs: '100%', sm: '300px' }, flexShrink: 0, textAlign: 'center' }}>
              <Image
                src={getImageUrl(movie.movie_poster)}
                alt={movie.title}
                width={300}
                height={450}
                priority
                style={{ width: '100%', height: 'auto', borderRadius: '8px', boxShadow: '0 4px 12px rgba(0,0,0,0.15)' }}
              />
            </Box>
            <Box>
              <Typography variant="h4" component="h1" gutterBottom fontWeight="bold">
                {movie.title}
              </Typography>
              {movie.rating !== null && (
                <Rating value={movie.rating} precision={0.5} readOnly size="large" sx={{ mb: 2 }} />
              )}
              {movie.genres && (
                <Box sx={{ display: 'flex', gap: 1, flexWrap: 'wrap', mb: 2 }}>
                  {movie.genres.split(',').map(genre => (
                    <Chip key={genre} label={genre.trim()} size="small" />
                  ))}
                </Box>
              )}
              <Typography variant="body1" sx={{ mb: 1 }}><strong>監督:</strong> {movie.director || '情報なし'}</Typography>
              <Typography variant="body1" sx={{ mb: 1 }}><strong>俳優:</strong> {movie.actors || '情報なし'}</Typography>
              <Typography variant="body1" sx={{ mb: 1 }}><strong>公開年:</strong> {movie.release_year || '情報なし'}</Typography>
              <Typography variant="body1" sx={{ mb: 1 }}><strong>制作国:</strong> {movie.country || '情報なし'}</Typography>
              <Typography variant="body1" sx={{ mb: 1 }}><strong>視聴日:</strong> {movie.watched_date || '情報なし'}</Typography>
               <Typography variant="body1" sx={{ mb: 1 }}><strong>視聴方法:</strong> {movie.watch_method || '情報なし'}</Typography>
            </Box>
          </Box>
          <Divider sx={{ my: 4 }} />
          <Box>
            <Typography variant="h5" gutterBottom>感想</Typography>
            <Typography variant="body1" sx={{ whiteSpace: 'pre-wrap' }}>{movie.impressions || '感想はありません。'}</Typography>
          </Box>
          {/* --- ここからボタン部分 --- */}
          <Box sx={{ mt: 4, display: 'flex', gap: 2, justifyContent: 'flex-end' }}>
            <Button component={Link} href="/movies/list" variant="outlined">
              リストに戻る
            </Button>
            {/* 削除ボタンを追加 */}
            <Button variant="contained" color="error" onClick={handleDeleteDialogOpen} disabled={isLoading}>
              削除
            </Button>
          </Box>
          {/* --- ここまでボタン部分 --- */}
        </Paper>
      </Container>

      {/* --- ここから削除確認ダイアログ --- */}
      <Dialog
        open={openDeleteDialog}
        onClose={handleDeleteDialogClose}
      >
        <DialogTitle>映画の記録を削除しますか？</DialogTitle>
        <DialogContent>
          <DialogContentText>
            「{movie.title}」の記録を完全に削除します。この操作は元に戻せません。
          </DialogContentText>
        </DialogContent>
        <DialogActions>
          <Button onClick={handleDeleteDialogClose}>キャンセル</Button>
          <Button onClick={handleDelete} color="error" disabled={isLoading}>
            {isLoading ? '削除中...' : '削除'}
          </Button>
        </DialogActions>
      </Dialog>
      {/* --- ここまで削除確認ダイアログ --- */}
    </>
  );
}